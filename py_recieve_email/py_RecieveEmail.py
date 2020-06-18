from email.parser import Parser
import poplib
from email.header import decode_header
from email.utils import parseaddr

class EMailConsole:
    def __init__(self, usr_account, usr_pwd, pop_address):
        self.usr_account = usr_account
        self.usr_pwd = usr_pwd
        self.pop_address = pop_address
        try:
            self.server = poplib.POP3_SSL(pop_address)
            
            self.server.user(usr_account)
            self.server.pass_(usr_pwd)
            
        except poplib.error_proto as e:
            print(e)
            print("login failed:" + str(e))
        
    def __decode_str(self, s):
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value

    def __guess_charset(self, msg):
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return charset 

    def getMailList(self):
        # list()返回所有邮件的编号:
        resp, self.mails, octets = self.server.list()
        return self.mails
    
    def getMailNum(self):
        self.mails = []
        resp, self.mails, octets = self.server.list()
        return len(self.mails) 
    
    def __parseEmail(self, index):
        resp, lines, octets = self.server.retr(index)
        # lines存储了邮件的原始文本的每一行,
        # 可以获得整个邮件的原始文本:
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        # 稍后解析出邮件:
        self.msg = Parser().parsestr(msg_content)
        return self.msg

    def getMailFrom(self, index):
        if self.getMailNum() >= index:
            tmp_msg = self.__parseEmail(index)
            value = tmp_msg.get("From","")
            if value:
                hdr, addr = parseaddr(value)
                name = self.__decode_str(hdr)
                value = u'%s <%s>' % (name, addr)
                self.fromStr = addr
                return self.fromStr
            else:
                return "None"

    def getMailSubject(self, index):
        if self.getMailNum() >= index:
            tmp_msg = self.__parseEmail(index)
            value = tmp_msg.get("Subject","")
            if value:
                value = self.__decode_str(value)
                self.subjectStr = value
                return self.subjectStr
            else:
                return "None"

    def __parseSinglePart(self, msg):
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = self.__guess_charset(msg)
            if charset:
                content = content.decode(charset)
            if content_type == "text/plain" or content_type == 'text/html':
                self.content = content
                return self.content
        else:
            return "None"

    def getMailContent(self, index):
        if self.getMailNum() >= index:
            msg = self.__parseEmail(index)
            if (msg.is_multipart()):
                parts = msg.get_payload()
                for n, part in enumerate(parts):
                    if 'text/plain' == part.get_content_type():
                        return self.__parseSinglePart(part)
            else:
                return self.__parseSinglePart(msg)
        else:
            return "None"

    def delMail(self, index):
        if self.getMailNum() >= index:
            self.server.dele(index)

    def loginIn(self):
        try:
            self.server = poplib.POP3_SSL(self.pop_address)
            self.server.user(self.usr_account)
            self.server.pass_(self.usr_pwd)
            return True
        except poplib.error_proto as e:
            print("login failed:" + str(e))
            return False

    def loginOut(self):
        self.server.quit()
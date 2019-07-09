import docx,re,os
pwd = os.getcwd()
address = pwd + "\\source"
filenames=os.listdir(address)
for filename in filenames:
    filepath = address+'\\'+filename
    document = docx.opendocx(filepath)  #打开文件demo.docx
    docx_lines = docx.getdocumenttext(document)
    docx_lines_num = len(docx_lines)
    for index,line in enumerate(docx_lines):
        if "growth" in line:
            # print(line)
            string = []
            now_index_head = index
            now_index_tail = index
            while True:
                now_index_head = now_index_head - 1
                if "来源" in docx_lines[now_index_head]:
                    # print("来源头：" + str(now_index_head))
                    break
            while True:
                now_index_tail = now_index_tail + 1
                if "来源" in docx_lines[now_index_tail]:
                    # print("来源尾：" + str(now_index_tail))
                    break
                if now_index_tail == (docx_lines_num -1):
                    # print("来源尾：" + str(now_index_tail))
                    break
            for i in docx_lines[now_index_head:now_index_tail]:
                # print(i)
                string.append(i + "\n")
            # print("\n")
            string.append("\n")
            print("".join(string))
            

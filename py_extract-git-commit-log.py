import os

def tagFormTag(tag_a, tag_b):
    if isinstance(tag_a,basestring) or isinstance(tag_b, basestring):
        return
    cmd = "git log --pretty="%s|" tag_a...tag_b >> D:\\temp.log"
    os.system(cmd)

tagFormTag("2.0.21", "2.0.20")
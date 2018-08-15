import subprocess
import shutil



langs={
    "js":["node","rhino"],
    "java":["javac"],
    "class":["java"],
    "sh":["sh"],
}
def topy(filepath,comp=None):
    filepath
    if comp == None:
        i = 0
        ext = filepath.rfind('.')

        ext2 = filepath.rfind('/')
        if ext2 > ext:
            ext = filepath[ext + 1:-1]
        else:
            ext = filepath[ext + 1:]
        lang = langs[ext][i]
        check = shutil.which(lang)
        while (check == None and i < len(langs[ext]) - 1):
            i += 1
            lang = langs[ext][i]
            check = shutil.which(lang)
    else:
        lang = comp
        check = shutil.which(lang)
    if (check == None):
        return "no supported compiler found!!!"
    else:
        output = subprocess.run([lang, filepath], stdout=subprocess.PIPE)
        result = list(output.stdout.decode('UTF-8').split())
        return result


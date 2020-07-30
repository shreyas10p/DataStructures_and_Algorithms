class MorseCodeTree(object):
    """docstring for MorseCodeTree"""
    MORSE_LIST = [None,'E','T','I','A','N','M','S','U','R','W','D','K','G','O','H','V','F',None,'L',None,'P','J','B','X','C','Y','Z','Q']

    def __init__(self):
        super(MorseCodeTree, self).__init__()
        self._treeSize = len(self.MORSE_LIST)

    def translate(self,code):
        codeList = code.split(' ')
        sentence = ''
        for code in codeList:
            codeLen = len(code)
            if(code is not ''):
                word = self.decodeCode(code)
                if(word is False):
                    return 'Not a valid Morse code'
                sentence += word
            else:
                sentence += ' '
        return sentence

    def decodeCode(self,word):
        codeLen = len(word)
        pointer = 0
        for i in range(codeLen):
            if(word[i] == '.'):
                pointer = ((2*pointer)+1)
            elif(word[i] == '-'):
                pointer = ((2*pointer)+2)
            if(pointer>self._treeSize or self.MORSE_LIST[pointer] is None):
                return False
        return self.MORSE_LIST[pointer]

if __name__ == '__main__':
    morseTree = MorseCodeTree()
    ans = morseTree.translate('- .-. . . ...  .- .-... .  ..-. ..- -.')
    print(ans)

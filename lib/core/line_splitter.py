def extract(text_file):
        '''Split text file into a list of lines'''
        try:
            raw_text = ''
            with open(text_file, 'r') as f:
                raw_text = f.read()
            return raw_text.split('\n')
        except:
            return ValueError(f"ERROR! Can't split {text_file}")

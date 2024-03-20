from backend.NLP.main.preprocessor import Preprocessor

if __name__ == "__main__":
    p = Preprocessor()
    print("Start preprocessing ... ")
    p.run()
    print("Done !")
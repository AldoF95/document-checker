from estimate import process_tokens
from preprocess import build_corpus, preproces_corpus, get_sample
from utils import scale, load_doc, remove_file



def calculate_level(filename):
    try:
        doc = load_doc(filename)
        if doc:
            #build corpus from docuemnt
            corpus = build_corpus(doc, doc.page_count)
            #close document after finishing building the corpus
            doc.close()
            #preprocess corpus: cleaning and tokenization
            tokens = preproces_corpus(corpus)
            #get sample if corpus too big
            sample = get_sample(tokens)
            #get the ratios
            awl_ratio, lfwl_ratio = process_tokens(sample)
            #calculate level
            scale_level = scale(awl_ratio, lfwl_ratio)
            #remove uploaded file from memory
            remove_file(filename)
            return (awl_ratio, lfwl_ratio, scale_level)
        else:
            remove_file(filename)
            return (400, "Wrong type", "Document is not pdf type.")
    except:
        remove_file(filename)
        return (400, "Error", "Something went wrong while processing the file")


""" if __name__=='__main__':
    print(calculate_level("tale056.pdf")) """




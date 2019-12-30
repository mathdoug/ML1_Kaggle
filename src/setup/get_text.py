import os


def get_text(id):
    """
    Detail:
        The function returns the full text of a given node
    Arguments:
        id -> integer
    Return:
        fulltext -> string

    """
    # Find the right path of the text folder
    filename = __file__
    while os.path.basename(filename) != "ML1_Kaggle":
        filename = os.path.dirname(filename)
    filename = os.path.join(filename, "node_information", "text")

    # Take the txt of the node
    id_text = str(id) + ".txt"
    filename = os.path.join(filename, id_text)

    # Read the text
    f = open(filename, "r", encoding='ISO-8859-1')
    fulltext = f.read()

    return fulltext


if __name__ == "__main__":
    print(get_text(300))

import string

#removes uncessary punctuation
def remove_punctuation(input_string):
    out_string = ''

    for item in input_string:
        if item not in string.punctuation:
            out_string += item
        else:
            continue

    return out_string

def test_remove_punctuation():
    assert remove_punctuation("I!!! want some??? sushi%^&") == "I want some sushi"

result = test_remove_punctuation()
print(result)


#prepares text for interpreting by separating string into a list
#of words
def prepare_text(input_string):

    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()

    return out_list

def test_prepare_text():
    assert prepare_text("I want some sushi!!!") == ["i", "want","some","sushi"]


result = test_prepare_text()
print(result)

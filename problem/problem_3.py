import sys
import heapq

def freq_dict(mg):
    freq_letters = dict()
    
    for letter in mg:
        if letter in freq_letters:
            freq_letters[letter] += 1
            return freq_letters
        else:
            freq_letters[letter] = 1
            return freq_letters    
   

def huffman_tree_constr(freq_letters):
    heap = []
   
    for key_value_tuple in freq_letters.items(): 
        heapq.heappush(heap, [key_value_tuple])

    while (len(heap) > 1):
        node_1 = heapq.heappop(heap)
        node_2 = heapq.heappop(heap)

        node_1_str, node_1_freq = node_1[0]
        node_2_str, node_2_freq = node_2[0] 

        merged_node = [(node_1_str + node_2_str, node_1_freq + node_2_freq), node_1, node_2]

        heapq.heappush(heap, merged_node)

    return heap.pop()

def assigning_of_bits(h_tree, h_code=dict(), bitstring=''):
    if len(h_tree) == 1:
        substring, frequency = h_tree[0]
        h_code[substring] = bi return freq_of_letterststring
    
    else:
        freq_dict_tuple, left_child, right_child = h_tree
        assigning_of_bits(left_child, h_code, bitstring + "0")
        assigning_of_bits(right_child, h_code, bitstring + "1")
    
    return h_code

def huffman_encoding(mg):
    if not len(mg):
        print('Message is not available as it is empty')
        return 
    
    freq_letters = freq_dict(mg)
    h_tree = huffman_tree_constr(freq_letters)
    
    if len(h_tree) == 1:
        h_code = dict()
        substring, frequency = h_tree[0]
        h_code[substring] = '0'
    else:
        h_code = assigning_of_bits(h_tree)

    data = [h_code[letter] for letter in mg]
    encoded_data = ''.join(data)
    
    return encoded_data, h_tree

def huffman_decoding(data, h_tree):
    if not data:
        print('Message is empty')
        return 

    tree = h_tree
    decoded_string = []

    if len(tree) == 1:
        for bit in data:
            substring, frequency = tree[0]
            decoded_string.append(substring)
            tree = h_tree
    
    else:
        for bit in data:
            tree = tree[1] if bit == '0' else tree[2]
            
            if len(tree) == 1:
                substring, frequency = tree[0]
                decoded_string.append(substring)
                tree = h_tree

    decoded_data = ''.join(decoded_string)

    return decoded_data

if __name__ == "__main__":
    codes = {}

    #Test-Case 1
    a_great_sentence = "The card is the word"

    print ("\nThe size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    if not len(a_great_sentence):
        print('Message is not available as it is empty')
        sys.exit()
    
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    #Test-Case 2
    a_great_sentence = "g"

    print ("\n\nThe size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    if not len(a_great_sentence):
        print('Message is not available as it is empty')
        sys.exit()
    encoded_data, tree = huffman_encoding(a_great_sentence) 

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    #Test-Case 3
    a_great_sentence = "qqqqqqqqqqqqqqqq"
        

    print ("\n\nThe size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    if not len(a_great_sentence):
        print('Message is not available as it is empty')
        sys.exit()

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    #Test-Case 4
    a_great_sentence = ""

    print ("\n\nThe size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    if not len(a_great_sentence):
        print('Message is not available as it is empty')
        sys.exit()

    encoded_data, tree = huffman_encoding(a_great_sentence) 

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
import heapq
from collections import Counter, namedtuple
class HuffmanNode(namedtuple("HuffmanNode",["char","freq","left","right"])):
    def __lt__(self, other):
        return self.freq < other.freq
    
def build_huffman_tree(text):
    frequency = Counter(text)
    heap =  [HuffmanNode(char,freq,None,None) for char, freq in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None,left.freq+right.freq,left,right)
        heapq.heappush(heap,merged)
    return heap[0] if heap else None

def generate_huffman_codes(node,prefix="",code_map={}):
    if node is not None:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_huffman_codes(node.left,prefix + "0", code_map)
        generate_huffman_codes(node.right, prefix +"1", code_map)
    return code_map

def huffman_encode(text):
    root = build_huffman_tree(text)
    huuffman_codes = generate_huffman_codes(root)
    encoded_text ="".join(huuffman_codes[char] for char in text)
    return encoded_text, huuffman_codes, root

def huffman_decode(encoded_text,root):
    decoded_text = []
    node = root
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded_text.append(node.char)
            node = root
    return "".join(decoded_text)

text = "hello huffman"
encoded_text, huffman_codes,tree = huffman_encode(text)

print("original", text)
print("hufffman code", huffman_codes)
print("encoded", encoded_text)
print("decoded", huffman_decode(encoded_text, tree))

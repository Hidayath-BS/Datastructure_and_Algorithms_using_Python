def compute_lps(pattern):
    """
    Computes the Longest Prefix Suffix (LPS) array for the pattern.
    
    Parameters:
    pattern (str): The pattern to preprocess.
    
    Returns:
    list: LPS array for the pattern.
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # Use previous LPS value
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    """
    Implements the KMP pattern matching algorithm.
    
    Parameters:
    text (str): The text in which the pattern is searched.
    pattern (str): The pattern to be found.
    
    Returns:
    list: Starting indices of occurrences of pattern in text.
    """
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    result = []
    
    i = j = 0  # Pointers for text and pattern
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:  # Pattern found
            result.append(i - j)
            j = lps[j - 1]  # Move to last matched prefix
        
        elif i < n and text[i] != pattern[j]:  # Mismatch case
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1  # Move to next character in text

    return result

# Example usage:
text = "ababcabcabababd"
pattern = "ababd"
print("Pattern found at indices:", kmp_search(text, pattern))

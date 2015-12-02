def capitals(word):
    cap_list = []
    for char_i in range(len(word)):
       if word[char_i] == word[char_i].upper():
          cap_list.append(char_i)
          
    return cap_list


if __name__ == "__main__":
	print capitals("GoOasdfASDFasdfASfadsfsdASDFBy")
j > i and j > k: 
                        resultant.append(j)
                        if i > k:
                            resultant.append(i)
                            resultant.append(k)
                        elif i < k:
                            resultant.append(k)
                            resultant.append(i)
                        
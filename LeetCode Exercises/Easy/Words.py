#--- Another Interview

class QueryStringFormater:

    def __init__(self, s):
        self.data = self.formater(s[1:])

    def formater(self, s):
        data = {}
        variables = s.split("&")

        for var in variables:
            equal_split = var.split("=")

            #value checks
            if len(equal_split) == 1:
                equal_split.append('true')
            elif equal_split[1] == '%\3F':
                equal_split[1] = "%"

            #converting in list if necessary
            if equal_split[0] in data and type(data[equal_split[0]]) == str: 
                data[equal_split[0]] = [data[equal_split[0]]]
            
            #adding value to key
            if equal_split[0] in data and type(data[equal_split[0]]) == list:
                data[equal_split[0]].append(equal_split[1])
            else:
                data[equal_split[0]] = equal_split[1]
                
        return data
    
    def unformater(self):
        obj = self.data
        builder = "?"
        for key in obj:
            if type(obj[key]) == str:
                if obj[key] == 'true':
                    builder += key
                else:
                    builder += key + "=" + (obj[key] if obj[key] != '%' else '%3F')
                builder += "&"
            else:
                for elem in obj[key]:
                    if elem == 'true':
                        builder += key
                    else:
                        builder += key + "=" + (elem if elem != '%' else '%3F')
                    builder += "&"
                
        return builder[:-1]
    

x = QueryStringFormater("?foo=hello&foo&div=%\3F")

print(x.data)
print(x.unformater())



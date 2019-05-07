user_0 = {
    'username': 'KR11_HOTH',
    'first': 'Kevin',
    'last': 'Anaro-Wood',
}
#
# # print(user_0['first'])
# for key, value in user_0.items():
#     print("\nKey: {}".format(key))
#     print("Value: {}".format(value))
#
favourite_languages = {
    'Kevin' : 'Python',
    'James' : 'C',
    'Valerie' : 'C++',
    'Aunty' : 'Perl',
}

# for name, language in favourite_languages.items():
#     print("{}'s favourite language is {}".format(name.title(), language.title()))

# for name in favourite_languages.keys():
#     print("{}".format(name.title()))
#
# for name in favourite_languages:
#     print("{}".format(name.title()))

# # Loop through each value in dictionary, if present and in our list of friends. Print special message
# friends = ['Kevin', 'Aunty']
# for name in favourite_languages:
#     print(name.title())
#
#     if name in friends:
#         print("Hey {}, I see your favourite language is {}".format(name, favourite_languages[name].title()))

# if 'erin' not in favourite_languages:
#     print('Erin please take our poll')

# # Print dictionary in order
# for name in sorted(favourite_languages):
#     print("{}".format(name))
#
# # Print dictionary with DISTINCT values
# for language in set(favourite_languages.values()):
#     print("{}".format(language))
#
# for key in favourite_languages:
#     print('{}'.format(key[key]))

rivers = {
    'nile' : 'egypt',
    'thames' : 'england',
    'amazon' : 'brazil',
}

for river in rivers:
    print("The river {} runs through {}".format(river.title(), rivers[river].title()))

for river in rivers:
    print(river)

for river in rivers:
    print(rivers[river].title())
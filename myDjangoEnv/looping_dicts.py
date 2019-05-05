# user_0 = {
#     'username': 'KR11_HOTH',
#     'first': 'Kevin',
#     'last': 'Anaro-Wood',
# }
#
# # print(user_0['first'])
# for key, value in user_0.items():
#     print("\nKey: {}".format(key))
#     print("Value: {}".format(value))

favourite_languages = {
    'Kevin' : 'Python',
    'James' : 'C',
    'Valerie' : 'C++',
    'Aunty' : 'Perl',
}

for name, language in favourite_languages.items():
    print("{}'s favourite language is {}".format(name.title(), language.title()))

# for name in favourite_languages.keys():
#     print("{}".format(name.title()))
#
# for name in favourite_languages:
#     print("{}".format(name.title()))

friends = ['Kevin', 'Aunty']
for name in favourite_languages:
    print(name.title())

    if name in friends:
        print("Hey {}, I see your favourite language is {}".format(name, favourite_languages[name].title()))
import re

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My super star task</title>
</head>
<body>
    <div id="block-with-links">
        <div id="google">
            <a href="www.google.com">
                Google
            </a>
        <div/>
        <div id="facebook">
            <a href="http://facebook.com/dign-in">
                Facebook
            </a>
        </div>
            <div id="amazon">
                <a href="amazon.com">
                    Amazon
                </a>
            </div>
        </div>
    </div>
</body>
</html>
'''
pattern = r'<div id="(\w+)">\s*<a href="(.*?)">\s*(.*?)\s*</a>'
matches = re.findall(pattern, html)
result = [(match[0], match[1], match[2]) for match in matches]
print(result)
#second part of the task
new_pattern = r'<div id="(\w+)">\s*<a href="(?:https?://)?(?:www\.)?([\w.-]+)">\s*(.*?)\s*</a>'
new_matches = re.findall(new_pattern, html)
new_result = [(new_match[0], new_match[1], new_match[2]) for new_match in new_matches]
print(new_result)


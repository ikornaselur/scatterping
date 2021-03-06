# Scatterping

A simple library with the goal of:

1. Have a simple payload to make requests from AWS Lambda, that the library makes sure to push up
2. Do requests from different configurable AWS Lambda regions and collect results
3. Draw a map in terminal with Drawille, showing different response times from different regions

## Why?

Why not? Want to experiment with things such as deploying simple Lambda
payloads from code, invoke multiple lambdas and collecting results from all of
them and drawing stuff out in the terminal. It's just a simple project to play
around with.

# Example

Not much so far, but at least it can print out a world map, using drawille and
an public domain svg, to terminal by width:

```
-> % p run python script.py
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⣶⣴⡿⠿⣿⣟⠋⠉⠉⠉⠉⠉⠉⣩⠛⠃⠀⠀⠀⠠⢤⣶⡶⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⢶⣶⣤⢄⣀⡀
⠀⠀⠀⢀⣠⠤⠤⠤⠤⠤⣀⡠⠤⠤⣞⣿⣛⣒⣦⣾⢿⣻⡿⠽⡓⢄⠀⠀⢈⡧⠀⠀⠀⣀⣰⠿⠁⠀⠠⠄⠀⠀⠀⠀⣠⠤⠤⢄⣀⡀⣀⢐⣿⣭⣡⣖⢴⡚⠉⠀⠀⠀⠈⠋⠙⠓⠚⠒⠦⠤⠒⠒⠢⠤⠤⠤⢤⣤⠤⣄⣀⡀
⠀⡠⠾⠋⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢀⡨⠔⠻⢏⣐⡺⡽⠟⠁⠀⢸⣀⡴⠚⠉⠀⠀⠲⠟⠂⠀⠀⠀⢀⠤⠊⡠⣾⠀⠈⠻⠟⠉⠁⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⢀⣻⡟⠂
⠼⠗⠞⠉⠁⠉⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⢄⡀⣠⠏⠀⠙⢻⡀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢀⣠⣦⠀⠘⣶⣦⣎⡹⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠉⠉⠀⣟⢫⠁
⠀⠀⠀⠀⠀⠀⢰⣧⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠛⠁⢀⣤⠤⣴⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣷⠷⠊⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⡀⠈⠛
⠀⠀⠀⠀⠀⢀⠞⠁⠀⠀⠀⠀⠀⠀⠀⢨⡿⣿⠦⠄⣠⠔⠾⠒⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠤⠽⢀⠤⣤⣶⣤⡀⠀⢠⠛⣚⠣⡀⠰⡫⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⣷⡤
⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠯⣀⣴⣙⣀⣻⠨⠟⠱⣎⡻⣉⣈⡉⠁⠀⠸⣼⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢯⡖⢾⣄⢀⣨⢷
⠀⠀⠀⠀⠀⠈⣦⡀⠀⠀⠀⠀⣀⣀⣀⣀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠉⠁⠀⠀⠈⠒⠤⡰⠪⠥⠤⡽⠃⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠁⠿⠛⠁
⠀⠀⠀⠀⠀⠀⠹⡷⡀⠀⢀⠎⠀⠀⠀⠘⠷⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠈⠯⣲⢦⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣁
⠀⠀⠀⠀⠀⠀⠀⠀⠻⣀⠘⢦⠴⡲⠈⠉⣻⢾⣥⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡱⡀⠀⠀⢀⡠⠃⠀⠀⠙⣇⠀⠀⣠⠞⠉⢢⠀⠀⠀⣖⡾⠉⠁⢁⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠲⢭⢱⠀⠀⣀⣠⡀⠀⠙⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢾⠤⣒⠉⠀⠀⠀⠀⠀⠘⡄⢸⠁⠀⠀⠀⠉⣦⣄⠈⡇⠀⠀⠸⣷⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠚⡞⠁⠃⠈⠉⠳⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢄⣀⣀⣀⡤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⡼⠁⠀⠀⠀⠀⠀⠀⠘⠻⠆⠀⠀⠀⢀⠻⣌⠋⠁⠀⣀⡋⠸⣷⠀⠀⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⠀⠀⠀⠀⠀⠀⢈⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠨⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⢿⠂⢠⠞⠁⣧⣤⠄⡦⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠋⠓⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⡜⠁⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⢵⣈⣓⠚⠸⠟⠀⠒⠘⠻⣍⠓⠦⣠⡷⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠓⠓⠛⢀⣠⣀⠉⣿⠉⠳⠄⠈⠻
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢄⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⡠⠞⢠⠞⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠉⠀⠓⠴⠋⡇⠀⠀⠀⠀⡀⠰
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⠤⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⢀⠇⠀⢸⣰⠁⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠙⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⣀⠀⠀⠀⠀⠀⢀⡜
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢲⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠓⠒⠋⠉⠈⠑⣇⠀⢀⡴⠋⠀⠀⠀⠀⠀⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠰⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡭⠁⠀⠀⠀⠀⣀⡤⠾⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢇⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠷⠤⠛
```

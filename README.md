## Details what he does:
The w_tv script takes active TV channels from the stalker database and creates three files:
1. m3u where the TV channels are divided into categories
2. m3u without grouping by category
3. Text file with a list of TV channels

The w_video script takes movies and TV shows from the stalker database which are already uploaded and creates three files:
1. m3u Films without serials broken down by category
2. m3u Serials without movies by category
3. m3u Movies without serials, categorization and any sorting

If you want to run my parser, you will need to install requirements
```
pip install -r requirements.txt
```
and write your data to the config.py
import pymysql
import config

#Подключения к БД Сталкера
db = pymysql.connect(host=config.host, user=config.user, password=config.password,
db='stalker_db', charset='utf8mb4')
cur = db.cursor()
#--
#Берём все фильмы без сериалов подставляя название категории + сортировка
cur.execute("""SELECT name,url,title FROM video,video_series_files,
cat_genre WHERE video.id = video_series_files.video_id AND 
video.cat_genre_id_1 = cat_genre.id AND is_series='0' AND video.accessed='1'
 ORDER BY title ASC,name ASC""")
result_film=cur.fetchall()
#--
#Берём все сериалы без фильмов подставляя название категории + сортировка
cur.execute("""SELECT name,url,title FROM video,video_series_files,cat_genre WHERE 
video.id = video_series_files.video_id AND video.cat_genre_id_1 = cat_genre.id 
AND is_series='1' AND video.accessed='1' ORDER BY url ASC, title ASC;""")
result_serial=cur.fetchall()
#--
#Берём все фильмы без сериалов и сортировки
cur.execute("""SELECT name,url FROM video,video_series_files WHERE 
video.id = video_series_files.video_id AND is_series='0' AND video.accessed='1';""")
result=cur.fetchall()
db.close()
#--
#Локализация категорий
cat_group = {
"action":"Боевик",
"adventure":"Приключения",
"drama":"Драма",
"comedy":"Комедия",
"family":"Семейный",
"musical":"Мюзикл",
"horror":"Ужасы",
"western":"Вестерн",
"kriminal":"Криминал",
"detectiv":"Детектив",
"sport":"Спорт",
"thriller":"Триллер",
"fantasy":"Фэнтези",
"fiction":"Фантастика",
"cam":"Камеры",
"criminal":"Криминал",
"biography":"Биографический",
"melodrama":"Мелодрама",
"historical":"Исторический",
"war film":"Военный",
"comics":"Комикс",
"cartoon":"Мультфильм"}
#--
#Создание обыного плейлиста
def for_luga(f_name,sql_res):
  with open(config.home+f_name,"w+") as f:
    f.write("#EXTM3U\n")
    for i in sql_res:
      f.write("\n#EXTINF:-1, "+i[0]+"\n"+i[1])
#--
#Создание плейлист с указанием категории фильма/сериала
def file_write(f_name,sql_res):
  with open(config.home+f_name,"w+") as f:
    f.write("#EXTM3U\n")
    for i in sql_res:
      f.write("\n#EXTINF:-1 group-title=\""+cat_group[i[2].lower()]+"\","+i[0]+"\n"+i[1])
#--
file_write("films_group.m3u",result_film)
file_write("serials_group.m3u",result_serial)
for_luga("films.m3u",result)
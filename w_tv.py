import pymysql
import config

#--Подключение к БД--
db = pymysql.connect(host=config.host, user=config.user,password=config.password,
                     db='stalker_db', charset='utf8mb4')
cur = db.cursor() # формируем курсор для работы с sql-запросами
#--
#--Получаем список включенных каналов
cur.execute("SELECT name,logo,cmd,tv_genre_id FROM itv where status='1' ORDER BY tv_genre_id ASC;")
result=cur.fetchall()
cur.execute("SELECT number,name,cmd from itv where status='1' ORDER BY number ASC;")
r_list=cur.fetchall()
db.close()
#--
#Локализируем жанр телеканала
group={
1:'Документальное',
2:'Развлекательное',
3:'Для Детей',
4:'Видео',
5:'Музыкальные',
6:'Новостные',
7:'Природа',
8:'Спорт',
19:'Для взрослых',
20:'Религиозные',
22:'Телемагазин',
23:'Кулинарный',
24:'Fashion'}
#--
#Пишем телеканалы групируя по жанру
with open(config.home+"group.m3u","w+") as f:
  f.write('#EXTM3U\n')
  for channel in result:
    f.write('\n#EXTINF:-1 logo="/misc/logos/320/'+str(channel[1])+'" group-title="'+str(group[channel[3]])+'" on-demand="1", '+str(channel[0])+'\n'+str(channel[2])+'\n')
#--
#Пишем телеканалы без групировки
with open(config.home+"smart.m3u","w+") as f:
  f.write('#EXTM3U\n')
  for channel in r_list:
    f.write('\n#EXTINF:-1 on-demand="1", '+str(channel[1])+'\n'+str(channel[2]+'\n'))
#--
#Пишем телеканалы одним списком в текстовик
with open(config.home+"channels.txt","w+",encoding="cp1251") as f:
  for channel in r_list:
    f.write(str(channel[0])+' '+str(channel[1])+'\n')
#--

create database youtube;
use youtube;

insert into videos (author, title, likes, dislikes) values ('Daniel Marques', 'Guerra dos Tronos', 300, 20);
insert into videos (author, title, likes, dislikes) values ('James Nelson','MySQL', 500, 100);
insert into videos (author, title, likes, dislikes) values ('Sandra Bock','Python', 1234, 99);
insert into videos (fk_author, title, likes, dislikes) values (4, 'Inteligência Artificial', 2993, 199);

insert into author (nome, born) values ('Daniel Marques', '1997-06-26');
insert into author (nome, born) values ('James Nelson', '2001-11-29');
insert into author (nome, born) values ('Sandra Bock', '1994-03-05');
insert into author(nome, born) values ('Bruno Campos','2002-07-19');

update videos set author=1 where idvideos=1;
update videos set author=2 where idvideos=2;
update videos set author=3 where idvideos=3;

select * from videos join author on videos.fk_author = author.idauthor;

select videos.title, author.nome from videos join author on videos.fk_author = author.idauthor; 

insert into seo (category) value ('front-end');
insert into seo (category) value ('back-end');
insert into seo (category) value ('series');

update videos set fk_seo=3 where idvideos=1; 
update videos set fk_seo=2 where idvideos=2;
update videos set fk_seo=2 where idvideos=3;
update videos set fk_seo= 2 where idvideos=4;
 
select * from videos join seo on videos.fk_seo = seo.idseo;
select videos.title, seo.category from videos join seo on videos.fk_seo = seo.idseo;
select videos.title, author.nome, seo.category from videos join seo on videos.fk_seo = seo.idseo join author on videos.fk_author = author.idauthor;

insert into playlist (nome_playlist) value ('Desenvolvimento Web'); 
insert into playlist (nome_playlist) value ('Banco de Dados MySQL');
insert into playlist (nome_playlist) value ('Ciência de Dados');
insert into playlist (nome_playlist) value ('Seriado Jogo dos Tronos');

insert into videos_playlist (fk_idvideos, fk_idplaylist) values (1, 4);

select * from playlist join videos_playlist join videos on videos.idvideos = videos_playlist.fk_idvideos on playlist.idplaylist = 4 = videos_playlist.idvideos_playlist;

update playlist set fk_author = 1 where idplaylist = 1;

select author.nome, author.born, videos.title, seo.category, playlist.nome_playlist from videos join author on author.idauthor = videos.idvideos join seo on seo.idseo = videos.fk_seo join playlist on playlist.fk_author  = videos.idvideos;

select * from author;
select * from videos;
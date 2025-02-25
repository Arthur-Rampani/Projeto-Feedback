CREATE DATABASE dbfeedback;
USE dbfeedback;
CREATE TABLE tbcomentario(
	cod_comentario int  auto_increment primary key, 
	nome varchar(80) not null, 
    comentario text not null, 
    data_comentario datetime not null);
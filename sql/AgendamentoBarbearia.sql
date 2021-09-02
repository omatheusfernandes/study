USE AgendamentoBarbearia

DROP TABLE cliente

CREATE TABLE cliente(
	cod_cliente INT NOT NULL,
	nome_cliente VARCHAR (20) NOT NULL,
	agendamento VARCHAR (10) NOT NULL
);

INSERT INTO cliente (cod_cliente, nome_cliente, agendamento)
VALUES	(001, 'Júlio Freitas', '2021-05-10'),
		(002, 'Gonzalo Alejandro', '2021-05-11'),
		(003, 'Cristiano Gracieri', '2021-05-12'),
		(004, 'Marcos Vinícius', '2021-05-13'),
		(005, 'Jamerson Araújo', '2021-05-14'),
		(006, 'Nélio Luz', '2021-05-15'),
		(007, 'Thiago Fagundes', '2021-05-16'),
		(008, 'Marlon Araújo', '2021-05-17'),
		(009, 'Emerson Neves', '2021-05-18'),
		(010, 'Yuri Trivellato', '2021-05-19')


SELECT TOP 10 cod_cliente, nome_cliente, agendamento
FROM cliente
ORDER BY agendamento DESC
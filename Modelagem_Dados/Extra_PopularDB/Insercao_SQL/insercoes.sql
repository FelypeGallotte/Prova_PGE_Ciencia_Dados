INSERT INTO Cliente (Nome, CPF) VALUES 
('João Pedro', '76561469542'),
('Gabriel Dantas', '73437424505'),
('Luiz Francisco', '01959448528');


INSERT INTO Procurador (Nome_procurador, Numero_OAB) VALUES  
('Carlos Santana', '124578-SP'),
('Miguel Santos', '654987-RJ'),
('Ricardo Almeida', '341876-RS');


INSERT INTO Processo (Numero_Processo, Status, Orgao_Responsavel, Assunto, Id_Cliente) VALUES 
('1000', 'Em andamento', 'Procuradoria-Geral do Estado', 'Licitação Pública', 2),
('1001', 'Concluído', 'Agência Nacional de Telecomunicações', 'Cobrança Indevida', 1),
('1003', 'Cancelado', 'Advocacia-Geral da União', 'Concurso Público',  3);


INSERT INTO Processo_Procurador (Id_Processo, Id_Procurador, Data_Inicio, Data_Fim) VALUES 
(1, 2, '2025-02-14', NULL),
(2, 1, '2024-12-14', '2025-02-20'),
(3, 3, '2024-10-14', '2025-01-07');

INSERT INTO Documentos(Id_Processo, Tipo_Documento, Nome_Documento) VALUES 
(1, 'Edital', 'Edital_Licitacao_1000.pdf'),
(2, 'Decisão', 'Resolucao_ANATEL_1001.pdf'),
(3, 'Decisão', 'Sentenca_Judicial_1003.pdf');

INSERT INTO Prazo (Id_Processo, Tipo_Prazo, Data_Vencimento, Status) VALUES 
(1, 'Data Limite para Recursos', '2025-03-10', 'Pendente'),
(2, 'Data de Audiência', '2025-01-15', 'Concluído'),
(3, 'Data Limite para Apresentação de Documentos', '2025-02-28', 'Vencido');
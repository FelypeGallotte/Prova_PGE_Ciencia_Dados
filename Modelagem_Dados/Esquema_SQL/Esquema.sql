CREATE TABLE Cliente (
    Id_Cliente INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(50) NOT NULL,
    CPF VARCHAR(11) UNIQUE NOT NULL
);

CREATE TABLE Procurador (
    Id_Procurador INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Procurador VARCHAR(50) NOT NULL,
    Numero_OAB VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE Processo (
    Id_Processo INT PRIMARY KEY AUTO_INCREMENT,
    Numero_Processo VARCHAR(20) UNIQUE,
    Status ENUM('Em andamento', 'Concluído', 'Cancelado'),
    Orgao_Responsavel VARCHAR(100),
    Assunto VARCHAR(50),
    Id_Cliente INT,
    CONSTRAINT FK_Processo_Cliente FOREIGN KEY (Id_Cliente)
        REFERENCES Cliente (Id_Cliente) ON DELETE CASCADE
);

CREATE TABLE Processo_Procurador (
    Id_Processo INT,
    Id_Procurador INT,
    Data_Inicio DATE NOT NULL,
    Data_Fim DATE,
    PRIMARY KEY (Id_Processo, Id_Procurador),
    CONSTRAINT FK_Processo_Procurador_Processo FOREIGN KEY (Id_Processo)
        REFERENCES Processo (Id_Processo) ON DELETE CASCADE,
    CONSTRAINT FK_Processo_Procurador_Procurador FOREIGN KEY (Id_Procurador)
        REFERENCES Procurador (Id_Procurador) ON DELETE CASCADE
);

CREATE TABLE Documentos (
    Id_Documento INT PRIMARY KEY AUTO_INCREMENT,
    Id_Processo INT NOT NULL,
    Tipo_Documento VARCHAR(70) NOT NULL,
    Nome_Documento VARCHAR(100) NOT NULL,
    CONSTRAINT FK_Documentos_Processo FOREIGN KEY (Id_Processo)
        REFERENCES Processo (Id_Processo) ON DELETE CASCADE
);

CREATE TABLE Prazo (
    Id_Prazo INT PRIMARY KEY AUTO_INCREMENT,
    Id_Processo INT NOT NULL,
    Tipo_Prazo VARCHAR(70) NOT NULL,
    Data_Vencimento DATE NOT NULL,
    Status ENUM('Pendente', 'Vencido', 'Concluído'),
    CONSTRAINT FK_Prazo_Processo FOREIGN KEY (Id_Processo)
        REFERENCES Processo (Id_Processo) ON DELETE CASCADE
);
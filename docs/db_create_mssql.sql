drop table contato;
drop table profissional;
drop table agendamentos;

CREATE TABLE [contato] (
  [id] uniqueidentifier PRIMARY KEY DEFAULT (NEWID()),
  [criado_em] datetime DEFAULT (getdate()),
  [nome] varchar(50) NOT NULL,
  [email] varchar(50) NOT NULL,
  [telefone] varchar(20) NOT NULL,
  [documento] varchar(14) DEFAULT (null),
  [endereco_rua] varchar(50) DEFAULT (null),
  [endereco_numero] varchar(10) DEFAULT (null),
  [endereco_bairro] varchar(50) DEFAULT (null),
  [endereco_cidade] varchar(50) DEFAULT (null),
  [endereco_uf] varchar(2) DEFAULT (null),
  [endereco_cep] varchar(8) DEFAULT (null),
  [endereco_complemento] varchar(50) DEFAULT (null),
  [observacao] nvarchar(255) DEFAULT (null)
)
GO

CREATE TABLE [profissional] (
  [id] uniqueidentifier PRIMARY KEY DEFAULT (NEWID()),
  [criado_em] datetime DEFAULT (getdate()),
  [nome] varchar(50) NOT NULL,
  [sala] varchar(20) NOT NULL,
  [especialidade] varchar(20) NOT NULL,
  [indisponibilidade] varchar(20)
)
GO

CREATE TABLE [agendamentos] (
  [id] uniqueidentifier PRIMARY KEY DEFAULT (NEWID()),
  [criado_em] datetime DEFAULT (getdate()),
  [contato_id] uniqueidentifier NOT NULL,
  [profissional_id] uniqueidentifier NOT NULL,
  [data] datetime NOT NULL,
  [duracao] integer NOT NULL,
  [observacao] nvarchar(255) DEFAULT (null)
)
GO

ALTER TABLE [agendamentos] ADD FOREIGN KEY ([contato_id]) REFERENCES [contato] ([id])
GO

ALTER TABLE [agendamentos] ADD FOREIGN KEY ([profissional_id]) REFERENCES [profissional] ([id])
GO

program EstatisticasNotas;

type
  TAluno = record
    nome: string;
    nota: real;
  end;

var
  alunos: array[1..3] of TAluno;
  i: integer;
  media, soma: real;

procedure LerAlunos;
begin
  for i := 1 to 3 do
  begin
    writeln('Digite o nome do aluno ', i, ':');
    readln(alunos[i].nome);
    writeln('Digite a nota do aluno ', i, ':');
    readln(alunos[i].nota);
  end;
end;

begin
  soma := 0;
  LerAlunos;
  for i := 1 to 3 do
    soma := soma + alunos[i].nota;
  media := soma / 3;
  writeln('Média da turma: ', media:0:2);
  for i := 1 to 3 do
    if alunos[i].nota >= media then
      writeln(alunos[i].nome, ' ficou acima ou igual à média.')
    else
      writeln(alunos[i].nome, ' ficou abaixo da média.');
end.
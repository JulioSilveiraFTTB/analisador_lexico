document.addEventListener("DOMContentLoaded", () => {
  const exampleCodes = {
    variables: `program VariaveisExemplo;
var
  idade: integer;
  nome: string;
  salario: real;
begin
  idade := 25;
  nome := 'Pascal';
  salario := 1250.75;
  writeln('Nome: ', nome, ', Idade: ', idade, ', Salario: ', salario);
end.`,
    conditionals: `program CondicionaisExemplo;
var
  nota: integer;
begin
  nota := 85;
  if (nota >= 60) then
  begin
    writeln('Aprovado');
  end
  else
  begin
    writeln('Reprovado');
  end;
end.`,
    loops: `program LoopsExemplo;
var
  i: integer;
begin
  for i := 1 to 5 do
  begin
    writeln('Iteração FOR: ', i);
  end;

  i := 1;
  while i <= 5 do
  begin
    writeln('Iteração WHILE: ', i);
    i := i + 1;
  end;
end.`,
  };

  const form = document.querySelector("form");
  const codeTextInput = document.getElementById("code-text-input");
  const fileInput = document.getElementById("file");
  let fileNameLabel = null;

  document.querySelectorAll(".example-btn").forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();
      const exampleKey = button.dataset.example;
      const code = exampleCodes[exampleKey];

      if (code && codeTextInput && form) {
        codeTextInput.value = code;
        fileInput.value = "";
        form.submit();
      }
    });
  });

  const clearButton = document.getElementById("clear-btn");
  if (clearButton && form) {
    clearButton.addEventListener("click", (e) => {
      e.preventDefault();
      if (fileInput) fileInput.value = "";
      if (codeTextInput) codeTextInput.value = "";
      form.reset();
      form.submit();
    });
  }

  const grouped = document.getElementById("results-section-grouped");
  const ordered = document.getElementById("results-section-ordered");
  document.querySelectorAll('input[name="view_mode"]').forEach((radio) => {
    radio.addEventListener("change", (e) => {
      if (e.target.value === "grouped") {
        if (grouped) grouped.style.display = "";
        if (ordered) ordered.style.display = "none";
      } else {
        if (grouped) grouped.style.display = "none";
        if (ordered) ordered.style.display = "";
      }
    });
  });

  if (fileInput) {
    fileInput.addEventListener("click", function () {
      if (fileNameLabel) {
        fileNameLabel.remove();
        fileNameLabel = null;
      }
    });

    fileInput.addEventListener("change", function () {
      if (!this.files.length) {
        if (!fileNameLabel) {
          fileNameLabel = document.createElement("span");
          fileNameLabel.id = "file-name";
          fileNameLabel.className = "file-name-label";
          fileNameLabel.textContent = "Nenhum arquivo escolhido";
          this.parentNode.insertBefore(fileNameLabel, this.nextSibling);
        }
      } else {
        if (!fileNameLabel) {
          fileNameLabel = document.createElement("span");
          fileNameLabel.id = "file-name";
          fileNameLabel.className = "file-name-label";
          this.parentNode.insertBefore(fileNameLabel, this.nextSibling);
        }
        fileNameLabel.textContent = this.files[0].name;
      }
    });
  }

  document.querySelectorAll(".help-icon").forEach((icon) => {
    icon.addEventListener("click", function (e) {
      e.stopPropagation();
      // Fecha outros tooltips
      document.querySelectorAll(".help-icon").forEach((i) => {
        if (i !== icon) i.classList.remove("active");
      });
      icon.classList.toggle("active");
    });
  });

  document.addEventListener("click", function () {
    document
      .querySelectorAll(".help-icon")
      .forEach((i) => i.classList.remove("active"));
  });
});

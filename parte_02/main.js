$("#soundboard_form").on("submit", function(event){
   event.preventDefault(); // o usuário precisa selecionar um valor diferente do default, senão não envia a requisição

	$.ajax({
		method: "POST",
		url: $(this).attr("action"),
		// envia uma variável soundboard_dropdown para os servidor,
		// pega o valor do soundboard_dropdown do HTML para preencher a variável que vai para o servidor
		data: {soundboard_dropdown: $("#soundboard_dropdown").val()},
		success: function(responseData) {
			// toca o áudio
			console.log(responseData)
			document.getElementById('soundboard_paragraph_result').textContent = JSON.stringify(responseData);
		}
	});
});
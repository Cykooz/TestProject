function init_models(options)
{
	$('#models menu a').live('click', function()
	{
		var a = $(this);
		var model_name = a.attr('href').replace('#model-', '');
		$.getJSON(options.get_data_url, {model_name: model_name}, function(data, textStatus, jqXHR)
		{
			var table = $('<table></table>');
			var head_tr = $('<tr></tr>');
			$.each(data.titles, function(i, title)
			{
				head_tr.append('<th>' + title + '</th>');
			});
			table.append(head_tr);
			$.each(data.rows, function(i, row)
			{
				var tr = $('<tr></tr>');
				$.each(row, function(i, value)
				{
					tr.append('<td>' + value + '</td>');
				});
				table.append(tr);
			});
			$('#model-data').html(table);
			$('#models menu a').removeClass('selected');
			a.addClass('selected');
		});
		return false;
	});

	$.getJSON(options.get_models_url, function(data, textStatus, jqXHR)
	{
		var menu = $('<menu></menu>');
		$.each(data, function(i, model)
		{
			var a = $('<a href="#model-' + model.name + '">' + model.title + '</a>');
			menu.append(a);
		});
		$('#models').html(menu);
		$('#models menu:first-child a:first-child').click();
	});
}
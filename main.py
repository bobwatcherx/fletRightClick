from flet import *
def main(page:Page):
	page.window_width=400

	value_text = Text("")

	page.add(
		# NOW CREATE GESTURE DETECTOR
		# FOR DETECT RIGHT CURSOR CLICK
		GestureDetector(
		mouse_cursor=MouseCursor.CONTEXT_MENU,
		content=Container(
			width=300,
			height=200,
			content=TextField(
				label="edit text",
				multiline=True,
				height=200,
				value=value_text.value

				)
			)
			),

		# AND CREATE TEXTFIELD FOR PASTE TEXT HERE
		TextField(
			label="paste here",
			
			)



		)
flet.app(target=main)

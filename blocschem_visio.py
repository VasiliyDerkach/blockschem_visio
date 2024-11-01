
#pip install aspose-diagram-python
# В этом примере кода показано, как создать блок-схему в Python.
import aspose.diagram
from aspose.diagram import *


def createFlowChart():
    # схема для диаграммы, которая будет создана
    diagram_object = Input(
        input_rectangles=[
            InputRectangle("A", "Manager"),
            InputRectangle("B", "Team Leader"),
            InputRectangle("C", "Team Member"),
            InputRectangle("D", "Team Member"),
            InputRectangle("E", "Team Member")
        ],
        input_connectors=[
            InputConnector("A", "B"),
            InputConnector("B", "C"),
            InputConnector("B", "D"),
            InputConnector("B", "E")
        ]
    )

    diagram = Diagram("D:\\Files\\BasicShapes.vss")
    page = diagram.pages[0]

    shape_names = {}

    # Добавление фигур и соединителей из схемы


for rectangle in diagram_object.InputRectangles:
    shape = Shape()
    shape_id = diagram.add_shape(shape, "Rectangle", 0)
    shape_names[rectangle.Name] = shape_id
    shape = page.shapes.get_shape(shape_id)
    shape.text.value.add(Txt(rectangle.Text))

for connector in diagram_object.InputConnectors:
    connector_id = diagram.add_shape(Shape(), "Dynamic connector", 0)
    page.connect_shapes_via_connector(
        shape_names[connector.OriginShapeName],
        aspose.diagram.manipulation.ConnectionPointPlace.RIGHT,
        shape_names[connector.DestinationShapeName],
        aspose.diagram.manipulation.ConnectionPointPlace.LEFT,
        connector_id
    )

layout_options = aspose.diagram.autolayout.LayoutOptions()
layout_options.layout_style = aspose.diagram.autolayout.LayoutStyle.FLOW_CHART
layout_options.direction = aspose.diagram.autolayout.LayoutDirection.LEFT_TO_RIGHT
layout_options.space_shapes = 5.0
layout_options.enlarge_page = True

diagram.layout(layout_options)

page.page_sheet.print_props.print_page_orientation.value = PrintPageOrientationValue.LANDSCAPE

save_options = aspose.diagram.saving.DiagramSaveOptions()
save_options.save_format = SaveFileFormat.VSDX
save_options.auto_fit_page_to_drawing_content = True

diagram.save("D:\\Files\\flowchart_output.vsdx", save_options)


class Input:
    def __init__(self, input_rectangles=None, input_connectors=None):
        self.InputRectangles = input_rectangles if input_rectangles else []
        self.InputConnectors = input_connectors if input_connectors else []


class InputRectangle:
    def __init__(self, name, text):
        self.Name = name
        self.Text = text


class InputConnector:
    def __init__(self, origin_shape_name, destination_shape_name):
        self.OriginShapeName = origin_shape_name
        self.DestinationShapeName = destination_shape_name


createFlowChart()
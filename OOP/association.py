# Relationships between classes: association, aggregation, and composition
# Association is a type of relationship where objects
# are connected within the system.
# This is the most common relationship between objects and has subsets
# like aggregation and composition (which we'll see later).
# Usually, we have an association when an object has
# an attribute that references another object.
# Association does not specify how an object controls
# the lifecycle of another object.
class Writer:
    def __init__(self, name) -> None:
        self.name = name
        self._tool = None

        @property
        def tool(self):
            return self._tool
        
        @tool.setter
        def tool(self, tool):
            self._tool = tool

class WritingTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return f'{self.name} is writing...'
    
writer = Writer('Verstappen')
pen = WritingTool('BIC pen')
typewriter = WritingTool('Typewriter')
writer.tool = typewriter

print(pen.write())
print(writer.tool.write())
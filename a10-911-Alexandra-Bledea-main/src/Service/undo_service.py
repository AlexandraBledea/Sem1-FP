

class UndoException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class UndoService:

    def __init__(self):
        self._history = []
        self._index = -1

    @staticmethod
    def create_new_update_operation(function_call, old_params, new_params):
        """
        With this function we create a new update operation
        :param function_call: will be the name of the update function
        :param old_params: the params before the change
        :param new_params: the params after the change
        :return: the operation
        """
        undo_function = FunctionCall(function_call, *old_params)
        redo_function = FunctionCall(function_call, *new_params)
        return Operation(undo_function, redo_function)

    @staticmethod
    def create_new_remove_operation(remove_call, remove_params, add_call, add_params):
        """
        With this function we create a new remove operation
        :param remove_call: will be the name of the remove function
        :param remove_params: the params necessarily for remove
        :param add_call: will be the name of the add function
        :param add_params: the params necessarily for add
        :return: the operation
        """
        undo_function = FunctionCall(add_call, *add_params)
        redo_function = FunctionCall(remove_call, *remove_params)
        return Operation(undo_function, redo_function)

    @staticmethod
    def create_new_add_operation(remove_call, remove_params, add_call, add_params):
        """
        With this function we create a new add operation
        :param remove_call: will be the name of the remove function
        :param remove_params: the params necessarily for remove
        :param add_call: will be the name of the add function
        :param add_params: the parmas necessarily for add
        :return: the operation
        """
        undo_function = FunctionCall(remove_call, *remove_params)
        redo_function = FunctionCall(add_call, *add_params)
        return Operation(undo_function, redo_function)

    @staticmethod
    def transform_into_cascading_operation(*operations):
        """
        With this function we transform more operations into a cascading operations
        :param operations: the operations which need to be done simultaneously
        :return: the cascaded operation
        """
        return CascadedOperation(*operations)

    def add_new_cascading_operation(self, *operations):
        """
        With this function we record a cascade operation
        :param operations: the operations which need to be done simultaneously
        :return: it doesn't return anything
        """
        self.record(self.transform_into_cascading_operation(*operations))

    def record(self, operation):
        """
        With this function we record each operation
        :param operation: represents the undo/redo operation created for a specific function call
        :return: it doesn't return anything
        """
        self._history = self._history[0:self._index + 1]
        self._history.append(operation)
        self._index += 1

    def undo(self):
        """
        With this function we implement the undo functionality
        :return: it doesn't return anything
        """
        if self._index == -1:
            raise UndoException("There are no operations to undo")

        operation = self._history[self._index]
        operation.undo()
        self._index -= 1

    def redo(self):
        """
        With this function we implement the redo functionality
        :return: It doesn't return anything
        """
        if self._index + 1 == len(self._history):
            raise UndoException("There are no operations to redo")

        self._index += 1
        operation = self._history[self._index]
        operation.redo()


class CascadedOperation:
    """
    Represents a cascaded operation (where 1 user operation corresponds to more than 1 program op)
    """

    def __init__(self, *operations):
        """
        :param operations: represents the cascade operations
        """
        self._operations = operations

    def undo(self):
        """
        With this function we go trough all the operations which were created as cascade and undo them one by one at a
        a single step
        :return: it doesn't return anything
        """
        for operation in self._operations:
            operation.undo()

    def redo(self):
        """
        With this function we go trough all the operations which were created as cascade and redo them one by one at a
        a single step
        :return: it doesn't return anything
        """
        for operation in self._operations:
            operation.redo()


class Operation:

    def __init__(self, function_undo, function_redo):
        """
        Here we create the operation which consists of an undo function and a redo function for a specific function call
        :param function_undo: undo function
        :param function_redo: redo function
        """
        self._function_undo = function_undo
        self._function_redo = function_redo

    def undo(self):
        self._function_undo()

    def redo(self):
        self._function_redo()


class FunctionCall:

    def __init__(self, function_name, *function_params):
        """
        :param function_name: the name of the function
        :param function_params: the parameters the function need to be called
        """
        self._function_name = function_name
        self._function_params = function_params

    def __call__(self):
        """
        Like that we call the function specified with its parameters
        :return: it doesn't return anything
        """
        self._function_name(*self._function_params)

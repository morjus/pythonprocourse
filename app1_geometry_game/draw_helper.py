def penup_always(func):

    def pen_up(*args, **kwargs):
        canvas = kwargs['canvas']
        canvas.penup()
        func(*args, **kwargs)
        canvas.penup()

    return pen_up

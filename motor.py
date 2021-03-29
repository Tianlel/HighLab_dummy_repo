class KCubeDCMotorSpyrelet(Spyrelet):
    requires = {
        'motor': KCubeDCMotor,
    }

    @Task()
    def goto_position(self):
        params = self.parameters.widget.get()
        self.motor.position = params['Position']
        return

    @Element()
    def parameters(self):
        params = [
                ('Position', {
                    'type': float,
                    'bounds': [-180, 180],
                    'default': 10,
                    }),
                ]
        w = ParamWidget(params)
        return w
    
    @Element()
    def save(self):
        w = RepositoryWidget(self)
        return w



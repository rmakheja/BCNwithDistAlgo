# -*- generated by 1.0.9 -*-
import da
PatternExpr_172 = da.pat.TuplePattern([da.pat.ConstantPattern('Pong')])
PatternExpr_177 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Pong')])])
PatternExpr_203 = da.pat.TuplePattern([da.pat.ConstantPattern('Ping')])
PatternExpr_208 = da.pat.FreePattern('ping')
_config_object = {}

class Ping(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._PingReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PingReceivedEvent_0', PatternExpr_172, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, pong, **rest_254):
        super().setup(pong=pong, **rest_254)
        self._state.pong = pong
        pass

    def run(self):
        self.send(('Ping',), to=self._state.pong)
        super()._label('_st_label_169', block=False)
        _st_label_169 = 0
        while (_st_label_169 == 0):
            _st_label_169 += 1
            if PatternExpr_177.match_iter(self._PingReceivedEvent_0, SELF_ID=self._id):
                _st_label_169 += 1
            else:
                super()._label('_st_label_169', block=True)
                _st_label_169 -= 1
        self.output('Ponged.')

class Pong(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._PongReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PongReceivedEvent_0', PatternExpr_203, sources=[PatternExpr_208], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, **rest_254):
        super().setup(**rest_254)
        pass

    def run(self):
        super()._label('_st_label_200', block=False)
        ping = None

        def ExistentialOpExpr_201():
            nonlocal ping
            for (_, (_, _, ping), (_ConstantPattern219_,)) in self._PongReceivedEvent_0:
                if (_ConstantPattern219_ == 'Ping'):
                    if True:
                        return True
            return False
        _st_label_200 = 0
        while (_st_label_200 == 0):
            _st_label_200 += 1
            if ExistentialOpExpr_201():
                _st_label_200 += 1
            else:
                super()._label('_st_label_200', block=True)
                _st_label_200 -= 1
        self.output('Pinged.')
        self.send(('Pong',), to=ping)

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])

    def run(self):
        pong = self.new(Pong, num=1, at='PongNode@172.24.17.74')
        ping = self.new(Ping, num=1)
        self._start(pong)
        self._start(ping)

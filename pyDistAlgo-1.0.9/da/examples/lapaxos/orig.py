# -*- generated by 1.0.9 -*-
import da
PatternExpr_215 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.BoundPattern('_BoundPattern218_'), da.pat.FreePattern(None)])
PatternExpr_222 = da.pat.FreePattern('a')
PatternExpr_250 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.BoundPattern('_BoundPattern253_'), da.pat.TuplePattern([da.pat.FreePattern('n2'), da.pat.FreePattern('v')])])
PatternExpr_281 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.BoundPattern('_BoundPattern284_'), da.pat.TuplePattern([da.pat.FreePattern('n2'), da.pat.FreePattern(None)])])
PatternExpr_317 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.BoundPattern('_BoundPattern320_'), da.pat.FreePattern(None)])
PatternExpr_324 = da.pat.FreePattern('a')
PatternExpr_365 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_370 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('done')])])
PatternExpr_410 = da.pat.TuplePattern([da.pat.ConstantPattern('prepare'), da.pat.FreePattern('n')])
PatternExpr_417 = da.pat.FreePattern('p')
PatternExpr_423 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.FreePattern('n2'), da.pat.FreePattern(None)])
PatternExpr_452 = da.pat.TuplePattern([da.pat.ConstantPattern('accepted'), da.pat.FreePattern('n'), da.pat.FreePattern('v')])
PatternExpr_478 = da.pat.TuplePattern([da.pat.ConstantPattern('accepted'), da.pat.FreePattern('n'), da.pat.FreePattern(None)])
PatternExpr_513 = da.pat.TuplePattern([da.pat.ConstantPattern('accept'), da.pat.FreePattern('n'), da.pat.FreePattern('v')])
PatternExpr_526 = da.pat.TuplePattern([da.pat.ConstantPattern('respond'), da.pat.FreePattern('n2'), da.pat.FreePattern(None)])
PatternExpr_562 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_567 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('done')])])
PatternExpr_610 = da.pat.TuplePattern([da.pat.ConstantPattern('accepted'), da.pat.FreePattern('n'), da.pat.FreePattern('v')])
PatternExpr_636 = da.pat.TuplePattern([da.pat.ConstantPattern('accepted'), da.pat.BoundPattern('_BoundPattern639_'), da.pat.BoundPattern('_BoundPattern640_')])
PatternExpr_643 = da.pat.FreePattern('a')
PatternExpr_788 = da.pat.TuplePattern([da.pat.ConstantPattern('learned')])
PatternExpr_793 = da.pat.BoundPattern('_BoundPattern794_')
PatternExpr_795 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern801_')]), da.pat.TuplePattern([da.pat.ConstantPattern('learned')])])
_config_object = {}
import sys
from random import randint
TIMEOUT = 1

class Proposer(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ProposerReceivedEvent_0 = []
        self._ProposerReceivedEvent_1 = []
        self._ProposerReceivedEvent_2 = []
        self._ProposerReceivedEvent_3 = []
        self._ProposerReceivedEvent_4 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_0', PatternExpr_215, sources=[PatternExpr_222], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_1', PatternExpr_250, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_2', PatternExpr_281, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_3', PatternExpr_317, sources=[PatternExpr_324], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_4', PatternExpr_365, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, acceptors, **rest_814):
        super().setup(acceptors=acceptors, **rest_814)
        self._state.acceptors = acceptors
        self._state.n = None
        self._state.majority = self._state.acceptors

    def run(self):
        while (not PatternExpr_370.match_iter(self._ProposerReceivedEvent_4, SELF_ID=self._id)):
            self.to_consent()
        self.output('terminating')

    def to_consent(self):
        self._state.n = ((0, self._id) if (self._state.n == None) else ((self._state.n[0] + 1), self._id))
        self.send(('prepare', self._state.n), to=self._state.majority)
        super()._label('_st_label_210', block=False)
        _st_label_210 = 0
        self._timer_start()
        while (_st_label_210 == 0):
            _st_label_210 += 1
            if (len({a for (_, (_, _, a), (_ConstantPattern233_, _BoundPattern235_, _)) in self._ProposerReceivedEvent_0 if (_ConstantPattern233_ == 'respond') if (_BoundPattern235_ == self._state.n)}) > (len(self._state.acceptors) / 2)):
                v = self.anyof(({v for (_, _, (_ConstantPattern269_, _BoundPattern271_, (n2, v))) in self._ProposerReceivedEvent_1 if (_ConstantPattern269_ == 'respond') if (_BoundPattern271_ == self._state.n) if (n2 == max({n2 for (_, _, (_ConstantPattern298_, _BoundPattern300_, (n2, _))) in self._ProposerReceivedEvent_2 if (_ConstantPattern298_ == 'respond') if (_BoundPattern300_ == self._state.n)}))} or {randint(1, 100)}))
                responded = {a for (_, (_, _, a), (_ConstantPattern335_, _BoundPattern337_, _)) in self._ProposerReceivedEvent_3 if (_ConstantPattern335_ == 'respond') if (_BoundPattern337_ == self._state.n)}
                self.send(('accept', self._state.n, v), to=responded)
                self.debug('### chose', self._state.n, v)
                _st_label_210 += 1
            elif self._timer_expired:
                self.output('failed proposal number', self._state.n)
                _st_label_210 += 1
            else:
                super()._label('_st_label_210', block=True, timeout=TIMEOUT)
                _st_label_210 -= 1

    def anyof(self, s):
        return (next(iter(s)) if s else None)

class Acceptor(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._AcceptorSentEvent_1 = []
        self._AcceptorSentEvent_2 = []
        self._AcceptorSentEvent_3 = []
        self._AcceptorSentEvent_5 = []
        self._AcceptorReceivedEvent_6 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_0', PatternExpr_410, sources=[PatternExpr_417], destinations=None, timestamps=None, record_history=None, handlers=[self._Acceptor_handler_409]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_1', PatternExpr_423, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_2', PatternExpr_452, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_3', PatternExpr_478, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_4', PatternExpr_513, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Acceptor_handler_512]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_5', PatternExpr_526, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_6', PatternExpr_562, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, learners, **rest_814):
        super().setup(learners=learners, **rest_814)
        self._state.learners = learners
        pass

    def run(self):
        super()._label('_st_label_559', block=False)
        _st_label_559 = 0
        while (_st_label_559 == 0):
            _st_label_559 += 1
            if PatternExpr_567.match_iter(self._AcceptorReceivedEvent_6, SELF_ID=self._id):
                _st_label_559 += 1
            else:
                super()._label('_st_label_559', block=True)
                _st_label_559 -= 1
        self.output('terminating')

    def anyof(self, s):
        "return any element of set s if s is not empty or 'None' otherwise"
        return (next(iter(s)) if s else None)

    def _Acceptor_handler_409(self, n, p):
        n2 = None

        def UniversalOpExpr_421():
            nonlocal n2
            for (_, _, (_ConstantPattern439_, n2, _)) in self._AcceptorSentEvent_1:
                if (_ConstantPattern439_ == 'respond'):
                    if (not (n > n2)):
                        return False
            return True
        if UniversalOpExpr_421():
            maxprop = self.anyof({(n, v) for (_, _, (_ConstantPattern468_, n, v)) in self._AcceptorSentEvent_2 if (_ConstantPattern468_ == 'accepted') if (n == max({n for (_, _, (_ConstantPattern493_, n, _)) in self._AcceptorSentEvent_3 if (_ConstantPattern493_ == 'accepted')}))})
            self.send(('respond', n, maxprop), to=p)
    _Acceptor_handler_409._labels = None
    _Acceptor_handler_409._notlabels = None

    def _Acceptor_handler_512(self, n, v):
        n2 = None

        def ExistentialOpExpr_524():
            nonlocal n2
            for (_, _, (_ConstantPattern542_, n2, _)) in self._AcceptorSentEvent_5:
                if (_ConstantPattern542_ == 'respond'):
                    if (n2 > n):
                        return True
            return False
        if (not ExistentialOpExpr_524()):
            self.send(('accepted', n, v), to=self._state.learners)
    _Acceptor_handler_512._labels = None
    _Acceptor_handler_512._notlabels = None

class Learner(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._LearnerReceivedEvent_0 = []
        self._LearnerReceivedEvent_1 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_LearnerReceivedEvent_0', PatternExpr_610, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_LearnerReceivedEvent_1', PatternExpr_636, sources=[PatternExpr_643], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, acceptors, **rest_814):
        super().setup(acceptors=acceptors, **rest_814)
        self._state.acceptors = acceptors
        pass

    def run(self):
        self.learn()
        self.output('terminating')
        self.send(('learned',), to=self.nodeof(self._id))

    def learn(self):
        super()._label('_st_label_607', block=False)
        a = n = v = None

        def ExistentialOpExpr_608():
            nonlocal a, n, v
            for (_, _, (_ConstantPattern627_, n, v)) in self._LearnerReceivedEvent_0:
                if (_ConstantPattern627_ == 'accepted'):
                    if (len({a for (_, (_, _, a), (_ConstantPattern654_, _BoundPattern656_, _BoundPattern657_)) in self._LearnerReceivedEvent_1 if (_ConstantPattern654_ == 'accepted') if (_BoundPattern656_ == n) if (_BoundPattern657_ == v)}) > (len(self._state.acceptors) / 2)):
                        return True
            return False
        _st_label_607 = 0
        self._timer_start()
        while (_st_label_607 == 0):
            _st_label_607 += 1
            if ExistentialOpExpr_608():
                self.output('learned', n, v)
                _st_label_607 += 1
            elif self._timer_expired:
                self.output('failed learning anything')
                _st_label_607 += 1
            else:
                super()._label('_st_label_607', block=True, timeout=(TIMEOUT * 10))
                _st_label_607 -= 1

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._Node_ReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_Node_ReceivedEvent_0', PatternExpr_788, sources=[PatternExpr_793], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def run(self):
        nacceptors = (int(sys.argv[1]) if (len(sys.argv) > 1) else 3)
        nproposers = (int(sys.argv[2]) if (len(sys.argv) > 2) else 5)
        nlearners = (int(sys.argv[3]) if (len(sys.argv) > 3) else 3)
        acceptors = self.new(Acceptor, num=nacceptors)
        proposers = self.new(Proposer, (acceptors,), num=nproposers)
        learners = self.new(Learner, (acceptors,), num=nlearners)
        for p in acceptors:
            self._setup(p, (learners,))
        self._start(((acceptors | proposers) | learners))
        super()._label('_st_label_779', block=False)
        l = None

        def UniversalOpExpr_780():
            nonlocal l
            for l in learners:
                if (not PatternExpr_795.match_iter(self._Node_ReceivedEvent_0, _BoundPattern801_=l)):
                    return False
            return True
        _st_label_779 = 0
        while (_st_label_779 == 0):
            _st_label_779 += 1
            if UniversalOpExpr_780():
                _st_label_779 += 1
            else:
                super()._label('_st_label_779', block=True)
                _st_label_779 -= 1
        self.output('done')
        self.send(('done',), to=(acceptors | proposers))

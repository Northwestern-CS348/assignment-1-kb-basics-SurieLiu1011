import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))
        for i in range(0, len(self.facts)):
            if fact == self.facts[i]:
                print("Already in KB")
                return
        for i in range(0, len(self.rules)):
            if fact == self.rules[i]:
                print("Already in KB")
                return
        if isinstance(fact, Fact):
            self.facts.append(fact)
        else:
            self.rules.append(fact)



        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        ListOfBinding = ListOfBindings()
        for i in range(0,len(self.facts)):
            #print(len(self.facts))
            #print(type(facts))
            #print(type(fact))
            answer = match(fact.statement, self.facts[i].statement)
            #print(fact.statement.terms)
            #print(self.facts[i].statement.terms)
            #print(i)
            if answer != False:
               ListOfBinding.add_bindings(answer)
        if len(ListOfBinding) == 0:
            return False
        return ListOfBinding







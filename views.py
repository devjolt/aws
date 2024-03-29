import inspect
import logging
import os
from pathlib import Path
import pkgutil
import platform
from random import randint, shuffle, choice
import re
import time

from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.shortcuts import render

from .cloud_practitioner_modules import cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp10 
from .utilities import utilities as utl
import question_logic as ql
from question_logic.all import *

logging.basicConfig(filename='cismp_question_logger.log', encoding='utf-8', level=logging.ERROR)
logging.disable(logging.INFO)

def populate_question_logic_dict()->dict:
    # make the path appropriately depending on OS
    if platform.system() == 'Windows':
        RESOURCE_INPUT_QUESTIONS_PATH = '\\resource_input_questions'
    else:
        RESOURCE_INPUT_QUESTIONS_PATH = '/resource_input_questions'
    
    # list the question logic files using imported ql
    pkgpath = os.path.dirname(ql.__file__)
    question_logic_files = [name for _, name, _ in pkgutil.iter_modules([pkgpath + RESOURCE_INPUT_QUESTIONS_PATH])]

    # put all logic files into a dictionary so we can use their logic
    question_logic_dict = {} # populating question logic dictionary
    for file_name in question_logic_files:
        if file_name not in ['all']:
            #print(file_name)
            exec(f"question_logic_dict['{file_name}']={file_name}.logic")
    return question_logic_dict

def generate_template_question_and_items(module:'object containing questions dict', key:str)->'template_question, items':
    if type(module.questions[key]) == dict:
        question_dict = module.questions[key] #get the dict
        if type(question_dict['type'])==str: # If resource type is just a string, there is only one.
            resource_type=question_dict['type']
        else: # resource type is a list/tuple 
            resource_type=choice(question_dict['type'])# and needs to be selected 
        print('resource_type:',resource_type)
        
        question_logic_dict = populate_question_logic_dict() # line 24ish in this file
        
        template_question, items = question_logic_dict[resource_type](question_dict)

    else:
        # Otherwise, we'd better assume we're using a set of unique question logic and try to use that.
        print('logic type question')# Self contained generating its own question and items.
        template_question, items = module.questions[key]()
    shuffle(items) # item order needs to be randomised
    return template_question, items 

module_str_to_name_dict = {
    'cp1':'introduction', 
    'cp2':'compute_in_the_cloud', 
    'cp3':'global_infrastructure_and_reliability', 
    'cp4':'networking',
    'cp5':'storage_and_databases',
    'cp6':'security',
    'cp7':'monitoring_and_analytics',
    'cp8':'pricing_and_support', 
    'cp9':'migration_and_innovation', 
    'cp10':'the_cloud_journey' 
}

module_name_to_module_code_dict = {
    'introduction':'cp1', 
    'compute_in_the_cloud':'cp2', 
    'global_infrastructure_and_reliability':'cp3', 
    'networking':'cp4',
    'storage_and_databases':'cp5',
    'security':'cp6',
    'monitoring_and_analytics':'cp7',
    'pricing_and_support':'cp8', 
    'migration_and_innovation':'cp9', 
    'the_cloud_journey':'cp10' 
}

module_object_to_name_dict = {
    cp1:'introduction', 
    cp2:'compute_in_the_cloud', 
    cp3:'global_infrastructure_and_reliability', 
    cp4:'networking',
    cp5:'storage_and_databases',
    cp6:'security',
    cp7:'monitoring_and_analytics',
    cp8:'pricing_and_support', 
    cp9:'migration_and_innovation', 
    cp10:'the_cloud_journey' 
}

module_str_to_object_dict = {
    'cp1':cp1, 
    'cp2':cp2, 
    'cp3':cp3, 
    'cp4':cp4,
    'cp5':cp5,
    'cp6':cp6,
    'cp7':cp7,
    'cp8':cp8, 
    'cp9':cp9, 
    'cp10':cp10 
}   

class HomeView(TemplateView):
    template_name = 'aws/home.html'

class ReportView(TemplateView):
    template_name = 'aws/report.html'

class CPView(TemplateView):
    template_name='aws/cp.html'

class RandomModuleView(TemplateView):
    modules = ()#set this in views
    template_name = 'aws/multichoice_module_cookies.html'
    
    def biased_module_picker(self):
        """currently does precisely nothing
        """
        val = randint(1, 100)
        if 1<=val<10:
            return  cp1
        elif 11<=val<20:
            return cp2
        elif 21<=val<30:
            return cp3
        elif 31<=val<40:
            return cp4
        elif 41<=val<50:
            return cp5
        elif 51<=val<60:
            return cp6
        elif 61<=val<70:
            return cp7
        elif 71<=val<80:
            return cp8
        elif 81<=val<90:
            return cp9
        else:
            return cp10
    
    def get_context_data(self, **kwargs):
        start = time.time() # Timing how long all this takes. We'll stop this timer later
        context = super().get_context_data(**kwargs) # make a context object to mess with.
        # 'modules' is a tuple containing module names passed into the view in urls.py. And we're picking one of them. 
        module = choice(self.modules)
        # Each module contains a dictionary called questions and we're picking one of the questions in that dictionary. 
        key = choice(tuple(module.questions.keys()))#from module, get key
        
        slashes = '\\\\' if platform.system() == 'Windows' else '/'# if running in windows, split with \\
        module_str=str(module).split(slashes)[-1][:-5] # and assuming anything else is Linux / 
         
        print(str(module)) # the only way we know what the module is
        print('module_str',module_str) # just checking we have the module code too
        print('key:',key) # and seeing what the key is

        question_type = 'multi-choice' # always multi choice at the moment, the logic for multi selection is broken!

        template_question, items = generate_template_question_and_items(module, key) # see above

        # Put question list and items in context dictionary.
        context['url'] = self.request.path
        context['question'], context['items'] = template_question, items
        context['question_type'] = question_type # Question type may tell the template how to handle the question if needed.
        context['question_description'] = key # Question key, acting as a question description
        context['cert_name'] = re.sub('[0-9]+', '', module_str)# needed in case we switch to specific question
        context['module_name'] = module_object_to_name_dict[module]# question module name needed as above
        context['module'] = module_object_to_name_dict[module]
        context['key'] = key
        context['title'] = 'AWS Cloud Practitioner Practice'# may change later...
        context['question_description_link'] = 'https://duckduckgo.com/?q=aws+' + key.replace('_', '+') # used to link if needed
        # We set this timer at the top so let's stop it now and see how long all that took!
        print('time taken:', time.time()-start)#interesting to know...
        return context

def SpecificAreaView(request, module_str, key):
    start = time.time() # Timing how long all this takes. Stopped and printed later
    module = module_str_to_object_dict[module_str]
    question_type = 'multi-choice' # the only question type we're using in this app at the moment!
    
    template_question, items = generate_template_question_and_items(module, key) # see above
    
    # Put question list and items in context dictionary.
    context={}
    context['url'] = request.path
    context['question'], context['items'] = template_question, items
    context['question_type'] = question_type # Question type may tell the template how to handle the question if needed.
    context['question_description'] = key # Question key, acting as a question description
    context['cert_name'] = re.sub('[0-9]+', '', module_str)# needed in case we switch to specific question
    context['module_name'] = module_object_to_name_dict[module]
    context['module'] = module_object_to_name_dict[module]
    context['key'] = key
    context['title'] = 'AWS ' + re.sub('_', ' ', module_object_to_name_dict[module]).capitalize()
    context['question_description_link'] = 'https://duckduckgo.com/?q=aws+' + key.replace('_', '+') # used to link if needed
    # We set this timer at the top so let's stop it now and see how long all that took!
    print('time taken:', time.time()-start)#interesting to know...
    return render(request, 'aws/multichoice_module_cookies.html', context)


def test_question(request):
    module_str = 'cp10'
    module = module_str_to_object_dict[module_str]
    key = 'AWS_Well-Architectured_Framework_concepts'
    question_logic = 'new_pairs'
    question_type = 'multi-choice'
    resource = module.questions[key]
    
    template_question, items = generate_template_question_and_items(module, key) # see above
    
    print('template_question', template_question)
    print('items', items)

    context = {}
    context['cert_name'] = re.sub('[0-9]+', '',module_str)
    context['question_description_link'] = 'https://duckduckgo.com/?q=aws+' + key.replace('_', '+')
    context['question'], context['items'] = template_question, items
    # Question type may tell the template how to handle the question if needed.
    context['question_type'] = question_type
    # Question key, acting as a question description
    context['question_description'] = key
    # question module name
    context['module_name'] = module_object_to_name_dict[module]
    # context['module_name'][f'{module_name_dict[module_str]}']
    context['title'] = 'Test'
    
    return render(request, 'aws/multichoice_module_cookies.html', context)
    


def log_problem(request):
    # post question details through
    # problem should include module, question key, question text and answer text
    # should get saved to a log
    other = request.POST.get('other')
    problem = request.POST.get('problem') if other == "" else other
    from_url = request.POST.get('url')
    module = request.POST.get('module')
    key = request.POST.get('key')
    question_type = request.POST.get('question_type')
    question = request.POST.get('question')
    items = request.POST.get('items')
    logging.error(f"AWS CP {problem} {module}, {key} ({question_type}): {question} - {items}")
    return HttpResponseRedirect(from_url)
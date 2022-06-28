import inspect
import os
from pathlib import Path
import pkgutil
import platform
from random import randint, shuffle, choice
import re
import time

from django.views.generic.base import TemplateView
from django.shortcuts import render

from .cloud_practitioner_modules import cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp10 
from .utilities import utilities as utl
import question_logic as ql
from question_logic.all import *

if platform.system() == 'Windows':
    SEARCH_PATTERN = "modules\\\\(.*?).py"
    RESOURCE_INPUT_QUESTIONS_PATH = '\\resource_input_questions'
else:
    SEARCH_PATTERN = "modules(.*?).py"
    RESOURCE_INPUT_QUESTIONS_PATH = '/resource_input_questions'

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
        # Timing how long all this takes, out of interest. We'll stop this timer later
        start = time.time()
        # We're going to mess with context data, so we make a context object to mess with.
        context = super().get_context_data(**kwargs)
        # 'modules' is a tuple containing module names passed into the view in urls.py. And we're picking one of them. 
        module = choice(self.modules)
        
        #changes search pattern depending on whether we're on Windows or Linux
        module_str = re.search(SEARCH_PATTERN, str(module))[1][1:]
        print('module_str',module_str)
        
        print('module_str:',module_str)
        # Each module contains a dictionary called questions and we're picking one of the questions in that dictionary. 
        key = choice(tuple(module.questions.keys()))#from module, get key
        print('key:',key)
        question_type = 'multi-choice'
        # v Uncomment to use a specific question in a specific module:
        #module = _1
        #key = 'test_question'
        # If chosen module and key contains a dict, we can use it directly to produce question and items
        if type(module.questions[key]) == dict:
            question_dict = module.questions[key]#get the dict
            
            # If resource type is just a string, there is only one.
            if type(question_dict['type'])==str:
                resource_type=question_dict['type']
            else:
                # Else, resource type is a list/tuple and needs to be selected.
                resource_type=choice(question_dict['type'])
            print('resource_type:',resource_type)

            # Seven different types of questions you can have... assuming that if a dict, it'll be one of them                        
            
            #makeing a list of all files in question logic module
            pkgpath = os.path.dirname(ql.__file__)
            question_logic_files = [name for _, name, _ in pkgutil.iter_modules([pkgpath + RESOURCE_INPUT_QUESTIONS_PATH])]
            
            question_logic_dict = {}

            for file_name in question_logic_files:
                if file_name not in ['all']:
                    #print(file_name)
                    exec(f"question_logic_dict['{file_name}']={file_name}.logic")
            
            """
            question_logic_dict = {
                'multi_option_from_correct_incorrect':utl.multi_option_from_correct_incorrect,
                'make_items_question_from_correct_incorrect':utl.make_items_question_from_correct_incorrect,
                'make_items_question_from_pairs':utl.make_items_question_from_pairs,
                'posneg_pairs':utl.posneg_pairs,
                'new_pairs':utl.new_pairs,
                'multi_option_pairs':utl.multi_option_pairs,
                'order_from_pairs':utl.order_from_pairs,
                'pairs_name_dict_attributes':utl.pairs_name_dict_attributes,
                'auto_correct_incorrect':utl.auto_correct_incorrect,
                'code_block_question':utl.code_block_question
                }
            """
            template_question, items = question_logic_dict[resource_type](question_dict)

        else:
            # Otherwise, we'd better assume we're using a set of unique question logic and try to use that.
            print('logic type question')# Self contained generating its own question and items.
            template_question, items = module.questions[key]()
    
        shuffle(items) # We don't want the order of the items to be predictable.
        # Put question list and items in dictionary.
        context['question'], context['items'] = template_question, items
        # Question type may tell the template how to handle the question if needed.
        context['question_type'] = question_type
        # Question key, acting as a question description
        context['question_description'] = key
        # question module name
        cert_str =  re.sub('[0-9]+', '', module_str)
        print(cert_str)
        context['cert_name'] = cert_str
        context['module_name'] = module_object_to_name_dict[module]
        # context['module_name'][f'{module_name_dict[module_str]}']
        context['title'] = 'AWS Cloud Practitioner Practice'
        key_link = key.replace(',', '')
        # what is this?
        context['key_link'] = key_link.replace(' ', '+').lower()
        # We set this timer at the top so let's stop it now and see how long all that took!
        
        #print('object to name:', module_object_to_name_dict[module])
        #print('str to name:', module_str_to_name_dict[module_str])
        stop = time.time()
        print('time taken:', stop-start)#interesting to know...
        return context

def SpecificAreaView(request, module_str, key):
    print(request.COOKIES['drill']  )
    module = module_str_to_object_dict[module_str]

    #should possible use a different template, without reset button or module cookies. A drill template?
    template_name = 'aws/multichoice_module_cookies.html'
    
    # Timing how long all this takes, out of interest. We'll stop this timer later
    start = time.time()
    # 'modules' is a tuple containing module names passed into the view in urls.py. And we're picking one of them. 
    print(module, key)
    question_type = 'multi-choice'
    # v Uncomment to use a specific question in a specific module:
    #module = _1
    #key = 'test_question'
    # If chosen module and key contains a dict, we can use it directly to produce question and items
    if type(module.questions[key]) == dict:
        question_dict = module.questions[key]#get the dict
        
        # If resource type is just a string, there is only one.
        if type(question_dict['type'])==str:
            resource_type=question_dict['type']
        else:
            # Else, resource type is a list/tuple and needs to be selected.
            resource_type=choice(question_dict['type'])
        print('resource_type:',resource_type)

        # Seven different types of questions you can have... assuming that if a dict, it'll be one of them                        
        
        #makeing a list of all files in question logic module
        pkgpath = os.path.dirname(ql.__file__)
        question_logic_files = [name for _, name, _ in pkgutil.iter_modules([pkgpath + RESOURCE_INPUT_QUESTIONS_PATH])]
        
        question_logic_dict = {}

        for file_name in question_logic_files:
            if file_name not in ['all']:
                print(file_name)
                exec(f"question_logic_dict['{file_name}']={file_name}.logic")
        
        """
        question_logic_dict = {
            'multi_option_from_correct_incorrect':utl.multi_option_from_correct_incorrect,
            'make_items_question_from_correct_incorrect':utl.make_items_question_from_correct_incorrect,
            'make_items_question_from_pairs':utl.make_items_question_from_pairs,
            'posneg_pairs':utl.posneg_pairs,
            'new_pairs':utl.new_pairs,
            'multi_option_pairs':utl.multi_option_pairs,
            'order_from_pairs':utl.order_from_pairs,
            'pairs_name_dict_attributes':utl.pairs_name_dict_attributes,
            'auto_correct_incorrect':utl.auto_correct_incorrect,
            'code_block_question':utl.code_block_question
            }
        """
        template_question, items = question_logic_dict[resource_type](question_dict)

    else:
        # Otherwise, we'd better assume we're using a set of unique question logic and try to use that.
        print('logic type question')# Self contained generating its own question and items.
        template_question, items = module.questions[key]()

    shuffle(items) # We don't want the order of the items to be predictable.
    # Put question list and items in dictionary.
    
    context={}
    context['question'], context['items'] = template_question, items
    # Question type may tell the template how to handle the question if needed.
    context['question_type'] = question_type
    # Question key, acting as a question description
    context['question_description'] = key
    
    context['cert_name'] = re.sub('[0-9]+', '', module_str)
        
    # question module name
    context['module_name'] = module_object_to_name_dict[module]
    context['title'] = 'AWS ' + re.sub('_', ' ', module_object_to_name_dict[module]).capitalize()  
    key_link = key.replace(',', '')
    # what is this?
    context['key_link'] = key_link.replace(' ', '+').lower()
    
    # We set this timer at the top so let's stop it now and see how long all that took!
    stop = time.time()
    print('time taken:', stop-start)#interesting to know...
    
    return render(request, 'aws/multichoice_module_cookies.html', context)


def test_question(request):
    print(request.COOKIES['drill']  )
    module_str = 'cp10'
    module = module_str_to_object_dict[module_str]

    key = 'AWS_Well-Architectured_Framework_concepts'
    question_logic = 'new_pairs'

    resource = module.questions[key]
    pkgpath = os.path.dirname(ql.__file__)
    question_logic_files = [name for _, name, _ in pkgutil.iter_modules([pkgpath + RESOURCE_INPUT_QUESTIONS_PATH])]
    print('question_logic_files', question_logic_files)
    question_type = 'multi-choice'
    if type(resource['type'])==str:
        resource_type=resource['type']
    else:
        # Else, resource type is a list/tuple and needs to be selected.
        resource_type=choice(resource['type'])
    print('resource_type:',resource_type)

    question_logic_dict = {}

    for file_name in question_logic_files:
        if file_name not in ['all']:
            exec(f"question_logic_dict['{file_name}']={file_name}.logic")

    print(question_logic_dict)

    #template_question, items = question_logic_dict[resource_type](resource)
    #template_question, items = question_logic_dict['posneg_pairs'](resource)
    template_question, items = question_logic_dict[question_logic](resource)

    print('template_question', template_question)
    print('items', items)

    context = {}
    context['cert_name'] = re.sub('[0-9]+', '',module_str)

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
    



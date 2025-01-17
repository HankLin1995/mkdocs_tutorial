from pathlib import Path
import os

def define_env(env):
    """
    This is the hook for defining variables, macros and filters
    """
    @env.macro
    def pdf_assets():
        return Path(env.conf['docs_dir']) / 'assets'

# PDF Configurations
pdf_style = {
    'font-family': 'Microsoft YaHei, sans-serif',
    'font-size': '12pt',
    'code-font-family': 'Consolas, monospace',
    'code-font-size': '10pt',
}

pdf_export_options = {
    'pdf_use_chinese': True,
    'pdf_font_path': [
        'C:\\Windows\\Fonts\\msyh.ttc',  # Microsoft YaHei
        'C:\\Windows\\Fonts\\simsun.ttc',  # SimSun as fallback
    ],
    'configuration': {
        'font_path': [
            'C:\\Windows\\Fonts\\msyh.ttc',
            'C:\\Windows\\Fonts\\simsun.ttc',
        ],
        'font_face': {
            'normal': 'Microsoft YaHei',
            'bold': 'Microsoft YaHei',
            'italic': 'Microsoft YaHei',
            'bold_italic': 'Microsoft YaHei'
        }
    }
}

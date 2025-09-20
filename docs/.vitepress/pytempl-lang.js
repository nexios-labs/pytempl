// Custom PyTemplate language definition for VitePress/Shiki
export const pytemplLanguage = {
  id: 'pytempl',
  scopeName: 'source.pytempl',
  patterns: [
    {
      include: '#comments'
    },
    {
      include: '#imports'
    },
    {
      include: '#component-definition'
    },
    {
      include: '#script-blocks'
    },
    {
      include: '#template-blocks'
    },
    {
      include: '#control-flow'
    },
    {
      include: '#component-calls'
    },
    {
      include: '#html-elements'
    },
    {
      include: '#interpolation'
    }
  ],
  repository: {
    comments: {
      patterns: [
        {
          name: 'comment.line.number-sign.pytempl',
          match: '#.*$'
        }
      ]
    },
    imports: {
      patterns: [
        {
          name: 'meta.import.pytempl',
          begin: '\\b(import|from)\\b',
          beginCaptures: {
            '1': {
              name: 'keyword.control.import.pytempl'
            }
          },
          end: '$',
          patterns: [
            {
              name: 'entity.name.namespace.pytempl',
              match: '\\b[a-zA-Z_][a-zA-Z0-9_.]*\\b'
            }
          ]
        }
      ]
    },
    'component-definition': {
      patterns: [
        {
          name: 'meta.component.definition.pytempl',
          begin: '\\b(component)\\s+([a-zA-Z_][a-zA-Z0-9_]*)\\s*(\\()',
          beginCaptures: {
            '1': {
              name: 'keyword.control.component.pytempl'
            },
            '2': {
              name: 'entity.name.function.component.pytempl'
            },
            '3': {
              name: 'punctuation.definition.parameters.begin.pytempl'
            }
          },
          end: '\\)',
          endCaptures: {
            '0': {
              name: 'punctuation.definition.parameters.end.pytempl'
            }
          }
        }
      ]
    },
    'script-blocks': {
      patterns: [
        {
          name: 'meta.script.python.pytempl',
          begin: '(<script)([^>]*type\\s*=\\s*["\']text/python["\'][^>]*)(>)',
          beginCaptures: {
            '1': {
              name: 'punctuation.definition.tag.begin.pytempl'
            },
            '2': {
              name: 'entity.other.attribute-name.pytempl'
            },
            '3': {
              name: 'punctuation.definition.tag.end.pytempl'
            }
          },
          end: '(</script>)',
          endCaptures: {
            '1': {
              name: 'punctuation.definition.tag.pytempl'
            }
          },
          contentName: 'source.python',
          patterns: [
            {
              include: 'source.python'
            }
          ]
        },
        {
          name: 'meta.script.javascript.pytempl',
          begin: '(<script)([^>]*type\\s*=\\s*["\']text/javascript["\'][^>]*|(?![^>]*type\\s*=\\s*["\']text/python["\'])[^>]*)(>)',
          beginCaptures: {
            '1': {
              name: 'punctuation.definition.tag.begin.pytempl'
            },
            '2': {
              name: 'entity.other.attribute-name.pytempl'
            },
            '3': {
              name: 'punctuation.definition.tag.end.pytempl'
            }
          },
          end: '(</script>)',
          endCaptures: {
            '1': {
              name: 'punctuation.definition.tag.pytempl'
            }
          },
          contentName: 'source.js',
          patterns: [
            {
              include: 'source.js'
            }
          ]
        }
      ]
    },
    'template-blocks': {
      patterns: [
        {
          name: 'meta.template.pytempl',
          begin: '(<template>)',
          beginCaptures: {
            '1': {
              name: 'punctuation.definition.tag.pytempl'
            }
          },
          end: '(</template>)',
          endCaptures: {
            '1': {
              name: 'punctuation.definition.tag.pytempl'
            }
          }
        }
      ]
    },
    'control-flow': {
      patterns: [
        {
          name: 'meta.control-flow.if.pytempl',
          begin: '\\b(if|elif)\\s+([^{]+)\\s*(\\{)',
          beginCaptures: {
            '1': {
              name: 'keyword.control.conditional.pytempl'
            },
            '2': {
              name: 'source.python.embedded.condition.pytempl'
            },
            '3': {
              name: 'punctuation.section.block.begin.pytempl'
            }
          },
          end: '\\}',
          endCaptures: {
            '0': {
              name: 'punctuation.section.block.end.pytempl'
            }
          }
        },
        {
          name: 'meta.control-flow.else.pytempl',
          begin: '\\b(else)\\s*(\\{)',
          beginCaptures: {
            '1': {
              name: 'keyword.control.conditional.pytempl'
            },
            '2': {
              name: 'punctuation.section.block.begin.pytempl'
            }
          },
          end: '\\}',
          endCaptures: {
            '0': {
              name: 'punctuation.section.block.end.pytempl'
            }
          }
        },
        {
          name: 'meta.control-flow.for.pytempl',
          begin: '\\b(for)\\s+([a-zA-Z_][a-zA-Z0-9_]*)\\s+(in)\\s+([^{]+)\\s*(\\{)',
          beginCaptures: {
            '1': {
              name: 'keyword.control.loop.pytempl'
            },
            '2': {
              name: 'variable.other.iterator.pytempl'
            },
            '3': {
              name: 'keyword.control.loop.pytempl'
            },
            '4': {
              name: 'source.python.embedded.iterable.pytempl'
            },
            '5': {
              name: 'punctuation.section.block.begin.pytempl'
            }
          },
          end: '\\}',
          endCaptures: {
            '0': {
              name: 'punctuation.section.block.end.pytempl'
            }
          }
        }
      ]
    },
    'component-calls': {
      patterns: [
        {
          name: 'meta.component.call.pytempl',
          begin: '(@)([a-zA-Z_][a-zA-Z0-9_]*)(\\()',
          beginCaptures: {
            '1': {
              name: 'punctuation.definition.component.pytempl'
            },
            '2': {
              name: 'entity.name.function.component.pytempl'
            },
            '3': {
              name: 'punctuation.definition.arguments.begin.pytempl'
            }
          },
          end: '\\)',
          endCaptures: {
            '0': {
              name: 'punctuation.definition.arguments.end.pytempl'
            }
          }
        }
      ]
    },
    'html-elements': {
      patterns: [
        {
          name: 'meta.tag.pytempl',
          begin: '(<)([a-zA-Z_][a-zA-Z0-9_-]*)',
          beginCaptures: {
            '1': {
              name: 'punctuation.definition.tag.begin.pytempl'
            },
            '2': {
              name: 'entity.name.tag.pytempl'
            }
          },
          end: '(/>)|(>)',
          endCaptures: {
            '1': {
              name: 'punctuation.definition.tag.end.pytempl'
            },
            '2': {
              name: 'punctuation.definition.tag.end.pytempl'
            }
          }
        },
        {
          name: 'meta.tag.closing.pytempl',
          match: '(</)([a-zA-Z_][a-zA-Z0-9_-]*)(>)',
          captures: {
            '1': {
              name: 'punctuation.definition.tag.begin.pytempl'
            },
            '2': {
              name: 'entity.name.tag.pytempl'
            },
            '3': {
              name: 'punctuation.definition.tag.end.pytempl'
            }
          }
        }
      ]
    },
    interpolation: {
      patterns: [
        {
          name: 'meta.interpolation.pytempl',
          begin: '\\{\\{',
          beginCaptures: {
            '0': {
              name: 'punctuation.definition.interpolation.begin.pytempl'
            }
          },
          end: '\\}\\}',
          endCaptures: {
            '0': {
              name: 'punctuation.definition.interpolation.end.pytempl'
            }
          },
          contentName: 'source.python.embedded.pytempl',
          patterns: [
            {
              include: 'source.python'
            }
          ]
        }
      ]
    }
  }
}

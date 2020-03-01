def check_paranthesis_balancing(paran_str, open, close, d):
      stack = []
      #Edge cases
      if len(paran_str) == 0:
            return 'no string provided to check paranthesis matching'

      elif len(paran_str) == 1:
            return 'paranthesis not balanced'

      elif len(paran_str)%2 != 0:
            return 'paranthesis not balanced'

      elif len(paran_str) > 1:
            for index, paranthesis in enumerate(paran_str):

                  if paranthesis in open:
                        stack.append(paranthesis)

                  if paranthesis in close:
                        #another tricky edge case
                        if index == 0 or len(stack) == 0:
                              return 'oye, paranthesis not balanced'

                        elif d[paranthesis] == stack[-1]:
                              stack.pop()
                              continue

                        else:
                              stack.append(paranthesis)

      return 'balanced' if stack == [] else 'not balanced'



paran_str = "{()}[]"
#'{[()()]}(('

d = { '}':'{',
      ']':'[',
      ')':'('
      }
open = d.values()
close = d.keys()

print(check_paranthesis_balancing(paran_str, open, close, d))
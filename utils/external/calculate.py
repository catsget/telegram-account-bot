import re

def calculate_expression(expr: str):
    expr = expr.replace(' ', '').replace('^', '**')
    try:
        if not re.fullmatch(r'^[\d+\-*/()**.]+$', expr):
            return "❌ Допустимы только цифры и +-*/^()."
        
        if expr.count('(') != expr.count(')'):
            return "❌ Несбалансированные скобки"
        
        result = eval(expr)
        return str(round(result, 4)) if isinstance(result, float) else str(result)
    
    except ZeroDivisionError:
        return "❌ Деление на ноль"
    except SyntaxError:
        return "❌ Неправильное выражение"
    except Exception:
        return "❌ Ошибка вычисления"
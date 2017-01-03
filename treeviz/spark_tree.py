import json

# Parser
def parse_tree(lines):
    block = []
    while lines :       
        if lines[0].startswith('If'):
            bl = ' '.join(lines.pop(0).split()[1:]).replace('(', '').replace(')', '')
            block.append({'name':bl, 'children':parse_tree(lines)})
            if lines[0].startswith('Else'):
                be = ' '.join(lines.pop(0).split()[1:]).replace('(', '').replace(')', '')
                block.append({'name':be, 'children':parse_tree(lines)})
        elif not lines[0].startswith(('If','Else')):
            block2 = lines.pop(0)
            block.append({'name':block2})
        else:
            break    
    return block
    
# Convert Tree to JSON
def tree_to_json(tree, features_names, file_path):
    tree = replace_features_names(tree, features_names)
    data = []
    for line in tree.splitlines() : 
        if line.strip():
            line = line.strip()
            data.append(line)
        else : break
        if not line : break
    res = []
    res.append({'name':'Root', 'children':parse_tree(data[1:])})
    with open(file_path, 'w') as outfile:
        json.dump(res[0], outfile)

def replace_features_names(tree, features_names):
    for i, name in enumerate(features_names):
        tree = tree.replace("feature {} ".format(i), name+' ')
    return tree
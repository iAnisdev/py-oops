def scope_test():
    def local():
        scope = 'local' # scope is local to local function only and will not affect the global scope
    def non_local():
        nonlocal scope # scope is non local and will affect the scope of the parent function but not sibling functions
        scope = 'non_local'
    def global_scope():
        global scope # scope is global and will affect the global scope only and will be accessible outside the function but not in the parent function or sibling functions
        scope = 'global'
    scope = 'test'
    print("At start , {}".format(scope))
    local()
    print(f"After assignment in local function , {scope}")
    non_local()
    print(f"After assignment in non local function , {scope}")
    global_scope()
    print(f"After assignment in global function , {scope}")
    
scope_test()

print(f"After function , {scope}")
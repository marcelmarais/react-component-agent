SHAD_CN_UI_DOCS = {
      'button': '''
      Name: Button
      Description: Displays a button or a component that looks like a button.
      Import: import { Button } from "@/components/ui/button"
      Usage examples:
      1. <Button variant="outline">Button</Button>
      2. <Button variant="secondary">Secondary</Button>
      3. <Button variant="outline" size="icon">
          <ChevronRightIcon className="h-4 w-4" />
        </Button>
      4.  <Button disabled> // LOADING BUTTON
            <ReloadIcon className="mr-2 h-4 w-4 animate-spin" />
            Please wait
          </Button>
      ''',
      'input': '''
      Name: Input
      Description: Displays a form input field or a component that looks like an input field.
      Import: import { Input } from "@/components/ui/input"
      Usage:
      1. <Input type="email" placeholder="Email" />
      2.  <div className="grid w-full max-w-sm items-center gap-1.5"> // File upload
            <Label htmlFor="picture">Picture</Label>
            <Input id="picture" type="file" />
          </div>
      '''
  }


SHAD_CN_UI_COMPONENTS = list(SHAD_CN_UI_DOCS.keys())
SHAD_CN_UI_COMPONENTS_STR = ', '.join(list(SHAD_CN_UI_DOCS.keys()))
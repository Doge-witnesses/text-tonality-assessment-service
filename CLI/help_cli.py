import click

@click.command()
def help():
    print("""
        ===Functions===
            
            - processing_text
            - processing_formatted_text
            - processing_logPart
    """)
    
if __name__ == "__main__":
    
    help()
import argparse
from Bio import Entrez
import pandas as pd
import re

# Set email and API Key (Replace with your own API key)
Entrez.email = "poptanikhushan@gmail.com"  # Your email
Entrez.api_key = "a6c8067e69367328cd57a3501b4113867007"  # Your API Key

# Keywords to filter company and non-academic affiliations
company_keywords = ["pharma", "biotech", "laboratories", "inc", "ltd", "gmbh", "corporation"]
academic_keywords = ["university", "college", "institute", "research center", "hospital", "school"]

def fetch_pubmed_papers(query, max_results=10, output_file=None, debug=False):
    """
    Fetch research papers from PubMed based on a search query.
    If output_file is provided, save results to CSV; otherwise, print to console.
    """
    if debug:
        print(f"DEBUG: Searching PubMed for query: '{query}' with max results: {max_results}")

    # Search PubMed
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()

    pmid_list = record["IdList"]

    if debug:
        print(f"DEBUG: Found {len(pmid_list)} papers")

    papers = []
    for pmid in pmid_list:
        # Fetch paper details
        handle = Entrez.efetch(db="pubmed", id=pmid, retmode="xml")
        paper_data = Entrez.read(handle)
        handle.close()

        for article in paper_data["PubmedArticle"]:
            title = article["MedlineCitation"]["Article"]["ArticleTitle"]
            journal = article["MedlineCitation"]["Article"]["Journal"]["Title"]
            pub_date = article["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"]
            year = pub_date.get("Year", "N/A")

            # Extract authors and affiliations
            author_list = article["MedlineCitation"]["Article"].get("AuthorList", [])
            non_academic_authors = []
            company_affiliations = []
            corresponding_author_email = "N/A"

            for author in author_list:
                if "AffiliationInfo" in author and author["AffiliationInfo"]:
                    affiliation = author["AffiliationInfo"][0].get("Affiliation", "").lower()

                    # Check for non-academic authors
                    if not any(word in affiliation for word in academic_keywords):
                        non_academic_authors.append(f"{author.get('LastName', '')} {author.get('ForeName', '')}")

                    # Check for company affiliations
                    if any(word in affiliation for word in company_keywords):
                        company_affiliations.append(affiliation)

                    # Extract email if present
                    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", affiliation)
                    if email_match:
                        corresponding_author_email = email_match.group(0)

            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": year,
                "Non-Academic Author(s)": ", ".join(non_academic_authors) if non_academic_authors else "N/A",
                "Company Affiliation(s)": ", ".join(company_affiliations) if company_affiliations else "N/A",
                "Corresponding Author Email": corresponding_author_email
            })

    # Convert to DataFrame
    df = pd.DataFrame(papers)

    if output_file:
        df.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")
    else:
        print(df.to_string(index=False))  # Print to console if no file specified

# Command-line argument parser
def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed research papers based on a query.")

    parser.add_argument("query", type=str, help="Search query for PubMed (e.g., 'Cancer Research')")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode to print additional information")
    parser.add_argument("-f", "--file", type=str, help="Specify the filename to save results (CSV format)")
    parser.add_argument("-n", "--num", type=int, default=10, help="Number of search results to retrieve (default: 10)")

    args = parser.parse_args()

    # Call the function with user inputs
    fetch_pubmed_papers(args.query, max_results=args.num, output_file=args.file, debug=args.debug)

# Run the script
if __name__ == "__main__":
    main()

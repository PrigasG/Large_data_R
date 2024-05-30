library(duckdb)
library(stringr)

process_file <- function(filename){
  df <- dbGetQuery(
    conn = dbConnect(duckdb()),
    statement = str_interp("
                           select *
                           from read_csv(
                           '${filename}',
                           header = true,
                           delim = ';',
                           parallel = true
                           )
                           ")
  )
}


df = process_file(filename = "FACILITY_Workbook.csv")
